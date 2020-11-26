from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass
class Vector:
    x: float
    y: float
    z: float

    def add(self, vector: Vector) -> Vector:
        return Vector(
            x=self.x + vector.x,
            y=self.y + vector.y,
            z=self.z + vector.z
        )

    def dotProduct(self, vector: Vector) -> float:
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    # self x vector
    def crossProduct(self, vector: Vector) -> Vector:
        return Vector(
            x=self.y * vector.z - self.z * vector.y,
            y=self.x * vector.z - self.z * vector.x,
            z=self.x * vector.y - self.y * vector.x
        )

    def multiply(self, scalar: float) -> Vector:
        return Vector(
            x=self.x * scalar,
            y=self.y * scalar,
            z=self.z * scalar
        )

    def divide(self, scalar: float) -> Vector:
        return Vector(
            x=self.x / scalar,
            y=self.y / scalar,
            z=self.z / scalar
        )

    def norm(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def unary(self) -> Vector:
        value = self.norm()
        if value > 1e-8:
            return Vector(
                x=self.x / value,
                y=self.y / value,
                z=self.z / value
            )
        else:
            return self

    def angle(self, vector: Vector) -> float:
        dot: float = math.fabs(self.dotProduct(vector=vector))
        if dot < 1e-8:
            return math.pi * 0.5
        else:
            return math.atan(self.crossProduct(vector=vector).norm() / dot)