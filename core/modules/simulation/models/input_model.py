from dataclasses import dataclass
from typing import Callable, List

from core.utils.math.models.vector_model import Vector
from core.modules.rocket.models.rocket_model import RocketModel

@dataclass
class Forces:
    drag: Callable[[float, float, Vector, float], Vector]
    weight: Callable[[float, float], Vector]
    thrust: Callable[[float, float, float, Vector], Vector]
    parachute_drag: Callable[[float, Vector, float], Vector]

@dataclass
class InitialCondition:
    velocity: Vector
    position: Vector
    atitude: Vector

    def toList(self) -> List[float]:
        return [
            self.position.x,
            self.position.y,
            self.position.z,
            self.velocity.x,
            self.velocity.y,
            self.velocity.z
        ]

@dataclass
class Input:
    forces: Forces
    rocket: RocketModel
    initial_condition: InitialCondition
    launch_rail_length: float
