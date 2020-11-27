# Python
from dataclasses import dataclass

# Utils
from ..utils.default_geometry import SURFACE_ROUGHNESS_DEFAULT

@dataclass
class TransitionModel:
    # Inputs
    height: float
    bottom_diameter: float
    top_diameter: float
    index: int
    surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT

    # Calculated
    cn: float = 0
    cp: float = 0

    def setCalculatedParameters(self, ref_diameter: float) -> None:
        self.cn = 2 * ((self.bottom_diameter / ref_diameter) ** 2 + (self.top_diameter / ref_diameter) ** 2)
        self.cp = (self.height / 3) * (1 + (1 - self.top_diameter / self.bottom_diameter) / (1 - (self.top_diameter / self.bottom_diameter) ** 2))
