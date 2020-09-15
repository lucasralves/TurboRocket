# Constant values
from core.models.geometry.constants import SURFACE_ROUGHNESS_DEFAULT

class FinModel:

    root_chord: float = 0.0
    tip_chord: float = 0.0
    span: float = 0.0
    number_of_fins: int = 0
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
            cn: float = 0.0,
            cp: float = 0.0,
            surface_roughness: float = SURFACE_ROUGHNESS_DEFAULT,
            index: int = 1):
        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.span = span
        self.number_of_fins = number_of_fins
        self.swept_angle = swept_angle
        self.surface_roughness = surface_roughness
        self.cn = cn
        self.cp = cp
        self.index = index