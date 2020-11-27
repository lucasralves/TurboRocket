# Enum
from core.modules.rocket.enums.nose_geometry import NoseGeometry

# Python
from dataclasses import dataclass

# Utils
from ..utils.default_geometry import SURFACE_ROUGHNESS_DEFAULT

@dataclass
class NoseModel:

    # Input
    height: float
    diameter: float
    geometry: NoseGeometry
    index: int
    surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT

    # Calculated
    cn: float = 0
    cp: float = 0

    def setCalculatedParameters(self) -> None:
        self.cn = 2
        if self.geometry == NoseGeometry.CONIC:
            self.cp = self.height * 0.666
        elif self.geometry == NoseGeometry.OGIVE:
            self.cp = self.height * 0.466
        else:
            self.cp = self.height * 0.466