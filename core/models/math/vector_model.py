from dataclasses import dataclass

@dataclass
class Vector:
    x: float
    y: float
    z: float

    def getX(self) -> float:
        return self.x