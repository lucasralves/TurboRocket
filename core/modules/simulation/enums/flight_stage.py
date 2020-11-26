from aenum import Enum, auto

class FlightStage(Enum):
    BASE = auto()
    LAUNCH_RAIL = auto()
    PROPELLED = auto()
    BALLISTIC = auto()
    PARACHUTE = auto()