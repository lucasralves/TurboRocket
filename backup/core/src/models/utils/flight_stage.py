from aenum import Enum, auto

class FlightStage(Enum):
    BASE = auto()
    PROPELLED_LAUNCH_RAIL = auto()
    PROPELLED_FREE_FLIGHT = auto()
    BALLISTIC_UP = auto()
    BALLISTIC_DOWN = auto()
    FIRST_PARACHUTE = auto()
    SECOND_PARACHUTE = auto()