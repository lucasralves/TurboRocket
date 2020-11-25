# Models
from core.models.rocket.nose_model import NoseModel
from core.models.rocket.body_model import BodyModel
from core.models.rocket.transition_model import TransitionModel
from core.models.rocket.fin_model import FinModel

# Helpers
from dataclasses import dataclass
from typing import List

@dataclass
class RocketModel:

    # Inputs
    nose: NoseModel
    bodies: List[BodyModel]
    transitions: List[TransitionModel]
    fins: List[FinModel]

    # calculated
    reference_area: float = 0
    surface_area: float = 0
    total_height: float = 0
    mean_surface_roughness: float = 0
    base_diameter: float = 0

    def setCalculatedParameters(self) -> None:
        self.reference_area = 0
        self.surface_area = 0
        self.total_height = 0
        self.mean_surface_roughness = 0
        self.base_diameter = 0