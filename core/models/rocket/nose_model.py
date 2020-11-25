# Enum
from core.models.rocket.nose_geometry import NoseGeometry

# Helpers
from dataclasses import dataclass

@dataclass
class NoseModel:

    # Input
    height: float
    diameter: float
    geometry: NoseGeometry
    surface_roughness: float
    index: int

    # Calculated
    cn: float = 0
    cp: float = 0

    def setCalculatedParameters(self) -> None:
        self.cn = 0
        self.cp = 0