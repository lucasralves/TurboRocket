# Models
from core.modules.rocket.models.nose_model import NoseModel
from core.modules.rocket.models.body_model import BodyModel
from core.modules.rocket.models.transition_model import TransitionModel
from core.modules.rocket.models.fin_model import FinModel
from core.utils.math.models.vector_model import Vector

# Aerodynamic
from core.modules.aerodynamic import DragCoefficientBarrowman

# Environment
from core.modules.environment.environment import EnvironmentModel

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

    # Coefficients
    cn_alpha: float = 0
    cm_alpha: float = 0
    cm_damping: float = 0
    cl_damping: float = 0

    def setCalculatedParameters(self) -> None:
        self.reference_area = 0
        self.surface_area = 0
        self.total_height = 0
        self.mean_surface_roughness = 0
        self.base_diameter = 0

    def calculateCd(self, altitude: float, velocity: Vector) -> float:
        reynolds: float = velocity.norm() * self.total_height * EnvironmentModel(altitude_ref=0).getDensity(altitude=altitude) / EnvironmentModel(altitude_ref=0).getViscosity(altitude=altitude)
        mach: float = velocity.norm() / EnvironmentModel(altitude_ref=0).getSoundSpeed(altitude=altitude)
        return DragCoefficientBarrowman(rocket=self).drag_coefficient(reynolds=reynolds, mach=mach)

    def calculateCn(self, altitude: float, velocity: Vector, atitude: Vector) -> float:
        angle: float = atitude.angle(vector=velocity.multiply(scalar=-1))
        return self.cn_alpha * angle