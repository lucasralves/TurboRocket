# Python libraries
from typing import List

# Models
from core.models.geometry.nose_model import NoseModel
from core.models.geometry.body_model import BodyModel
from core.models.geometry.transition_model import TransitionModel
from core.models.geometry.fin_model import FinModel


class RocketModel:

    # Geometry parameters
    reference_area: float
    surface_area: float
    total_height: float
    mean_surface_roughness: float
    base_diameter: float

    # Geometry models
    nose: NoseModel
    bodies: List[BodyModel]
    transitions: List[TransitionModel]
    fins: List[FinModel]

    def __init__(
            self,
            nose: NoseModel,
            bodies: List[BodyModel],
            transitions: List[TransitionModel],
            fins: List[FinModel]):
        self.nose = nose
        self.bodies = bodies
        self.transitions = transitions
        self.fins = fins
        self.calculate_base_diameter()

    def calculate_base_diameter(self):
        self.base_diameter = 0.0
        return