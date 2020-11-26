# Python packages
import math

# Helpers
from dataclasses import dataclass

@dataclass
class ConstantWindModel:
    speed_ref: float = 0.0

    def getWindSpeed(self) -> float:
        return self.speed_ref

@dataclass
class PowerWindModel:
    speed_ref: float = 1.0
    height_ref: float = 2.0
    exponent: float = 0.14

    def getWindSpeed(self, altitude_agl: float) -> float:
        if self.height_ref < 1e-8:
            return 0.0
        else:
            return self.speed_ref * ((altitude_agl / self.height_ref) ** self.exponent)

@dataclass
class LogarithmicWindModel:
    speed_ref: float = 2.0
    height_ref: float = 6.0
    plane_displacement: float = 1.0
    surface_roughness: float = 0.5

    def getWindSpeed(self, altitude_agl: float) -> float:
        if self.surface_roughness > 1e-8 and (altitude_agl - self.plane_displacement) > 1e-8 and (self.height_ref - self.plane_displacement) > 1e-8 and math.fabs(math.log((self.height_ref - self.plane_displacement) / self.surface_roughness)) > 1e-8:
            return self.speed_ref * math.log(
                (altitude_agl - self.plane_displacement) / self.surface_roughness) / math.log(
                (self.height_ref - self.plane_displacement) / self.surface_roughness)
        else:
            return 0.0

@dataclass
class WindModel:
    constant_wind: ConstantWindModel
    power_wind: PowerWindModel
    logarithmic_wind: LogarithmicWindModel
