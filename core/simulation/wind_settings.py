# Python libraries
from dataclasses import dataclass

@dataclass()
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

    def constantModel(self):
        return

    def powerModel(self):
        return

    def logarithmicModel(self):
        return
