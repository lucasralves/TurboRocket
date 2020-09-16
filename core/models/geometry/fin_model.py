# Python packages
import math

# Constant values
from core.models.geometry.constants import SURFACE_ROUGHNESS_DEFAULT

class FinModel:

    trailing_edge_area: float
    leading_edge_diameter: float
    thickness_pressure_drag_cdtt: float
    thickness_pressure_drag_epsilon: float
    one_fin_lateral_area: float
    trailing_edge_diameter: float = 0.0
    root_chord: float = 0.0
    tip_chord: float = 0.0
    span: float = 0.0
    number_of_fins: int = 0
    max_thickness: float = 0
    swept_angle: float = 0.0
    cn: float = 0.0
    cp: float = 0.0
    surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT
    index: int = 1

    def __init__(
            self,
            root_chord: float = 0.0,
            tip_chord: float = 0.0,
            span: float = 0.0,
            number_of_fins: int = 0,
            swept_angle: float = 0.0,
            max_thickness: float = 0.0,
            trailing_edge_diameter: float = 0.0,
            cn: float = 0.0,
            cp: float = 0.0,
            surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT,
            index: int = 1):
        self.trailing_edge_diameter = trailing_edge_diameter
        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.span = span
        self.number_of_fins = number_of_fins
        self.swept_angle = swept_angle
        self.surface_roughness = surface_roughness
        self.max_thickness = max_thickness
        self.cn = cn
        self.cp = cp
        self.index = index
        self.trailing_edge_area = span * trailing_edge_diameter / math.cos(swept_angle * math.pi / 180)
        self.leading_edge_diameter = max_thickness
        self.one_fin_lateral_area = (root_chord + tip_chord) * span * 0.5
        self.thickness_pressure_drag_epsilon = (self.one_fin_lateral_area / (span ** 2)) * ((max_thickness / root_chord) ** (1 / 3))
        self.thickness_pressure_drag_cdtt = 1.15 * ((max_thickness / root_chord) ** (5 / 3)) * (1.61 + self.thickness_pressure_drag_epsilon - math.sqrt(((self.thickness_pressure_drag_epsilon - 1.43) ** 2) + 0.578))