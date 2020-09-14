# Python libraries
from dataclasses import dataclass

# Constant values
from core.models.geometry.constants import SURFACE_ROUGHNESS_DEFAULT
from core.models.geometry.constants import NOSE_DEFAULT_GEOMETRY


@dataclass()
class NoseModel:

    height: float = 0.0
    diameter: float = 0.0
    geometry: str = NOSE_DEFAULT_GEOMETRY
    cn: float = 0.0
    cp: float = 0.0
    surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT
    index: int = 1

    def __init__(
            self,
            height: float = 0.0,
            diameter: float = 0.0,
            geometry: str = NOSE_DEFAULT_GEOMETRY,
            cn: float = 0.0,
            cp: float = 0.0,
            surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT,
            index: int = 1):
        self.height = height
        self.diameter = diameter
        self.surface_roughness = surface_roughness
        self.geometry = geometry
        self.cn = cn
        self.cp = cp
        self.index = index