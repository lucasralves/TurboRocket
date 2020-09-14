# Python libraries
from dataclasses import dataclass

# Constant values
from core.models.geometry.constants import SURFACE_ROUGHNESS_DEFAULT


@dataclass()
class TransitionModel:

    height: float = 0.0
    bottom_diameter: float = 0.0
    top_diameter: float = 0.0
    cn: float = 0.0
    cp: float = 0.0
    surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT
    index: int = 1

    def __init__(
            self,
            height: float = 0.0,
            bottom_diameter: float = 0.0,
            top_diameter: float = 0.0,
            cn: float = 0.0,
            cp: float = 0.0,
            surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT,
            index: int = 1):
        self.height = height
        self.bottom_diameter = bottom_diameter
        self.top_diameter = top_diameter
        self.surface_roughness = surface_roughness
        self.cn = cn
        self.cp = cp
        self.index = index