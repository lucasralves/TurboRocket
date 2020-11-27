# Python
from dataclasses import dataclass

# Utils
from ..utils.default_geometry import SURFACE_ROUGHNESS_DEFAULT

@dataclass
class BodyModel:

    # Inputs
    height: float
    diameter: float
    index: int
    surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT

    # Calculated
    cn: float = 0
    cp: float = 0

    def setCalculatedParameters(self) -> None:
        self.cn = 0
        self.cp = self.height * 0.5