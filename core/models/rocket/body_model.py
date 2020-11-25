# Helpers
from dataclasses import dataclass

@dataclass
class BodyModel:

    # Inputs
    height: float
    diameter: float
    surface_roughness: float
    index: int

    # Caluclated
    cn: float = 0
    cp: float = 0

    def setCalculatedParameters(self) -> None:
        self.cn = 0
        self.cp = 0