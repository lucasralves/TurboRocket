# Python packages
import math

# Helpers
from dataclasses import dataclass

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
    surface_roughness: float
    index: int
    
    # Calculated
    cn: float = 0
    cp: float = 0
    trailing_edge_area: float = 0
    one_fin_lateral_area: float = 0
    thickness_pressure_drag_cdtt: float = 0
    thickness_pressure_drag_epsilon: float = 0

    def setCalculatedParameter(self) -> None:

        # Calculated from inputs
        self.trailing_edge_area = self.span * self.trailing_edge_diameter / math.cos(self.swept_angle * math.pi / 180)
        self.one_fin_lateral_area = (self.root_chord + self.tip_chord) * self.span * 0.5
        self.thickness_pressure_drag_epsilon = (self.one_fin_lateral_area / (self.span ** 2)) * ((self.max_thickness / self.root_chord) ** (1 / 3))
        self.thickness_pressure_drag_cdtt = 1.15 * ((self.max_thickness / self.root_chord) ** (5 / 3)) * (1.61 + self.thickness_pressure_drag_epsilon - math.sqrt(((self.thickness_pressure_drag_epsilon - 1.43) ** 2) + 0.578))
        
        # Aerodynamic
        self.cp = 0
        self.cn = 0