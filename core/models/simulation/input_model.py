# Python packages
from dataclasses import dataclass
from typing import List

# Models
from core.models.math.vector_model import Vector

@dataclass
class InputModel:
    position: Vector
    velocity: Vector
    altitude: float

    def toList(self) -> List[float]:
        return [
            self.position.x,
            self.position.y,
            self.position.z,
            self.velocity.x,
            self.velocity.y,
            self.velocity.z
        ]

