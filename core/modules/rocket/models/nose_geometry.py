from aenum import Enum, auto

class NoseGeometry(Enum):
    OGIVE = auto()
    PARABOLIC = auto()
    CONIC = auto()