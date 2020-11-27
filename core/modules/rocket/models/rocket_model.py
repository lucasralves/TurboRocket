# Models
from core.modules.rocket.models.nose_model import NoseModel
from core.modules.rocket.models.body_model import BodyModel
from core.modules.rocket.models.transition_model import TransitionModel
from core.modules.rocket.models.fin_model import FinModel

# Helpers
from dataclasses import dataclass
from typing import List, Any

# Python
import math

# Utils
from core.utils.math.utils.conversions import LENGTH_MM_TO_M, AREA_MM2_TO_M2


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

    def setCalculatedParameters(self, cg: float) -> None:

        total_height: float = 0
        base_diameter: float = 0
        items: int = 0
        mean_surface_roughness: float = 0
        surface_area: float = 0

        # Set parts parameters

        # Nose
        self.nose.setCalculatedParameters()
        total_height += self.nose.height
        mean_surface_roughness = (mean_surface_roughness * items + self.nose.surface_roughness) / (items + 1)
        items += 1
        surface_area += 0.5 * math.pi * (self.base_diameter ** 2 + self.nose.height ** 2) * self.nose.diameter

        # Body
        for i in range(len(self.bodies)):
            self.bodies[i].setCalculatedParameters()
            total_height += self.bodies[i].height
            base_diameter = self.bodies[i].diameter
            mean_surface_roughness = (mean_surface_roughness * items + self.bodies[i].surface_roughness) / (items + 1)
            items += 1
            surface_area += self.bodies[i].height * math.pi * self.bodies[i].diameter

            # Transition
        for i in range(len(self.transitions)):
            self.transitions[i].setCalculatedParameters(ref_diameter=self.nose.diameter)
            total_height += self.transitions[i].height
            mean_surface_roughness = (mean_surface_roughness * items + self.transitions[i].surface_roughness) / (items + 1)
            items += 1
            surface_area += self.transitions[i].height * math.pi * (self.transitions[i].top_diameter + self.transitions[i].bottom_diameter)

        # Fin
        fin_diameter: float
        for i in range(len(self.fins)):
            fin_diameter = list(filter(lambda x: x.index == self.fins[i].index, self.bodies))[0].diameter
            self.fins[i].setCalculatedParameters(diameter=fin_diameter)
            mean_surface_roughness = (mean_surface_roughness * items + self.fins[i].surface_roughness) / (items + 1)
            items += 1
            surface_area += 0.5 * self.fins[i].span * (self.fins[i].root_chord + self.fins[i].tip_chord)

        self.reference_area = 0.25 * math.pi * (self.nose.diameter ** 2)
        self.surface_area = surface_area
        self.total_height = total_height
        self.mean_surface_roughness = mean_surface_roughness
        self.base_diameter = base_diameter

        # Set the aerodynamic coefficients
        self.aerodynamicCoefficients(cg=cg)

        # Correct units
        self.changeToCorrectUnit()

    def aerodynamicCoefficients(self, cg: float):

        # The fins must be added at last, because when list is sorted, they must be after the body
        list_parts: List[Any] = [self.nose] + self.bodies + self.transitions + self.fins
        list_parts.sort(key=lambda x: x.index)

        tip_position: float = 0
        cn_alpha: float = 0
        cm_alpha: float = 0
        for i in range(len(list_parts)):

            # Increase tip height
            if not isinstance(list_parts[i], FinModel):
                tip_position += list_parts[i].height

            cn_alpha += list_parts[i].cn
            cm_alpha += list_parts[i].cn * (cg - (tip_position + list_parts[i].cp))

        self.cn_alpha = cn_alpha
        self.cm_alpha = cm_alpha

    def changeToCorrectUnit(self):
        self.reference_area = self.reference_area * AREA_MM2_TO_M2
        self.surface_area = self.surface_area * AREA_MM2_TO_M2
        self.total_height = self.total_height * LENGTH_MM_TO_M
        self.base_diameter = self.base_diameter * LENGTH_MM_TO_M

        self.cm_alpha = self.cm_alpha * LENGTH_MM_TO_M