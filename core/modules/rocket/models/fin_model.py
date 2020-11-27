# Python packages
import math
from dataclasses import dataclass

# Utils
from ..utils.default_geometry import SURFACE_ROUGHNESS_DEFAULT

@dataclass
class FinModel:

    # Inputs
    leading_edge_diameter: float
    trailing_edge_diameter: float
    root_chord: float
    tip_chord: float
    span: float
    number_of_fins: int
    max_thickness: float
    swept_angle: float
    index: int
    surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT
    
    # Calculated
    cn: float = 0
    cp: float = 0
    diameter: float = 0
    trailing_edge_area: float = 0
    one_fin_lateral_area: float = 0
    thickness_pressure_drag_cdtt: float = 0
    thickness_pressure_drag_epsilon: float = 0

    def setCalculatedParameters(self, diameter: float) -> None:

        # Calculated from inputs
        self.trailing_edge_area = self.span * self.trailing_edge_diameter / math.cos(self.swept_angle * math.pi / 180)
        self.one_fin_lateral_area = (self.root_chord + self.tip_chord) * self.span * 0.5
        self.thickness_pressure_drag_epsilon = (self.one_fin_lateral_area / (self.span ** 2)) * ((self.max_thickness / self.root_chord) ** (1 / 3))
        self.thickness_pressure_drag_cdtt = 1.15 * ((self.max_thickness / self.root_chord) ** (5 / 3)) * (1.61 + self.thickness_pressure_drag_epsilon - math.sqrt(((self.thickness_pressure_drag_epsilon - 1.43) ** 2) + 0.578))

        # Geometry
        self.diameter = diameter

        # Aerodynamic
        self.cn = (1 + self.diameter / (2 * self.span + self.diameter)) * (4 * self.number_of_fins * ((self.span / self.diameter) ** 2) / (1 + math.sqrt(1 + (2 * math.sqrt(self.span ** 2 + (self.span * math.tan(self.swept_angle * math.pi / 180) + 0.25 * (self.tip_chord - self.root_chord)) ** 2) / (self.root_chord + self.tip_chord)) ** 2)))
        self.cp = ((self.span * math.sqrt(self.swept_angle * math.pi / 180)) / 3) * (self.root_chord + 2 * self.tip_chord) / (self.root_chord + self.tip_chord) + (1 / 6) * ((self.root_chord + self.tip_chord) - (self.root_chord * self.tip_chord) / (self.root_chord + self.tip_chord))