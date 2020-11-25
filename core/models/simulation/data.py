# Python packages
from dataclasses import dataclass
from typing import List
# Models
from core.models.math.vector_model import Vector

@dataclass
class Data:
    position: Vector
    velocity: Vector
    time: float

    def updateFromList(self, t: float, y: List[float]):
        self.updateTime(value=t)
        self.updatePosition(x=y[0], y=y[1], z=y[2])
        self.updateVelocity(x=y[3], y=y[4], z=y[5])

    def updateTime(self, value: float):
        self.time = value

    def updatePosition(self, x: float, y: float, z: float):
        self.position = Vector(x=x, y=y, z=z)

    def updateVelocity(self, x: float, y: float, z: float):
        self.velocity = Vector(x=x, y=y, z=z)