# Python packages
import math

# Math
from core.math.constants import ZERO_ERROR

class WindSettings:
    speed_ref: float = 0.0
    height_ref: float = 0.0
    exponent: float = 0.0
    plane_displacement: float = 0.0
    surface_roughness: float = 0.0

    def __init__(
            self,
            speed_ref: float = 0.0,
            height_ref: float = 0.0,
            exponent: float = 0.0,
            plane_displacement: float = 0.0,
            surface_roughness: float = 0.0):
        self.speed_ref = speed_ref
        self.height_ref = height_ref
        self.exponent = exponent
        self.plane_displacement = plane_displacement
        self.surface_roughness = surface_roughness

    def constantModel(self) -> float:
        return self.speed_ref

    def powerModel(self, altitude: float) -> float:
        try:
            return self.speed_ref * ((altitude / self.height_ref) ** self.exponent)
        except ZeroDivisionError:
            return 0.0

    def logarithmicModel(self, altitude: float) -> float:
        if (altitude - self.plane_displacement) > ZERO_ERROR and (self.height_ref - self.plane_displacement) > ZERO_ERROR:
            try:
                return self.speed_ref * math.log((altitude - self.plane_displacement) / self.surface_roughness) / math.log(
                    (self.height_ref - self.plane_displacement) / self.surface_roughness)
            except ZeroDivisionError:
                return 0.0
        else:
            return 0.0
