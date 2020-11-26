from __future__ import annotations
from aenum import Enum, auto

from core.modules.environment.utils.environment_constants import TROPOSPHERE_INITIAL_HEIGHT,\
    TROPOSPHERE_FINAL_HEIGHT, LOW_STRATOSPHERE_INITIAL_HEIGHT,LOW_STRATOSPHERE_FINAL_HEIGHT,\
    HEIGHT_STRATOSPHERE_INITIAL_HEIGHT, HEIGHT_STRATOSPHERE_FINAL_HEIGHT

class AtmosphereZone(Enum):
    NONE: auto()
    TROPOSPHERE = auto()
    LOW_STRATOSPHERE = auto()
    HEIGHT_STRATOSPHERE = auto()

    @staticmethod
    def getZone(altitude: float) -> AtmosphereZone:
        if TROPOSPHERE_INITIAL_HEIGHT <= altitude < TROPOSPHERE_FINAL_HEIGHT:
            return AtmosphereZone.TROPOSPHERE
        
        if LOW_STRATOSPHERE_INITIAL_HEIGHT <= altitude <= LOW_STRATOSPHERE_FINAL_HEIGHT:
            return AtmosphereZone.LOW_STRATOSPHERE

        if HEIGHT_STRATOSPHERE_INITIAL_HEIGHT < altitude <= HEIGHT_STRATOSPHERE_FINAL_HEIGHT:
            return AtmosphereZone.HEIGHT_STRATOSPHERE

        return AtmosphereZone.NONE