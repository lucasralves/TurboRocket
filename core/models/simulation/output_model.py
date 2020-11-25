# Python packages
from dataclasses import dataclass
from typing import List

# Models
from core.models.math.vector_model import Vector

@dataclass
class OutputModel:
    time: List[float]
    position: List[Vector]
    velocity: List[Vector]

    def insertFromList(self, t: float, y: List[float]):
        self.insertTime(value=t)
        self.insertPosition(x=y[0], y=y[1], z=y[2])
        self.insertVelocity(x=y[3], y=y[4], z=y[5])

    def insertTime(self, value: float):
        self.time.append(value)

    def insertPosition(self, x: float, y: float, z: float):
        self.position.append(Vector(x=x, y=y, z=z))

    def insertVelocity(self, x: float, y: float, z: float):
        self.velocity.append(Vector(x=x, y=y, z=z))