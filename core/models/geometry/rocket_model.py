# Python libraries
from typing import List

# Models
from core.models.geometry.nose_model import NoseModel
from core.models.geometry.body_model import BodyModel
from core.models.geometry.transition_model import TransitionModel
from core.models.geometry.fin_model import FinModel

class RocketModel:

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