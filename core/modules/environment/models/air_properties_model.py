# 1) This class calculates the temperature, pressure and density according to
# the International Standard Atmosphere
# 2) The viscosity is calculated as a function of temperature

##############################################################################
# Python Packages
import math
from scipy.interpolate import interp1d

# Helpers
from dataclasses import dataclass

# Enum
from ..enums.atmosphere_zone import AtmosphereZone

# Constants
from ..utils.environment_constants import AIR_GAMMA, AIR_GAS_CONSTANT, GRAVITY_ACCELERATION, EARTH_RADIUS
from ..utils.environment_constants import TROPOSPHERE_INITIAL_TEMPERATURE, \
    TROPOSPHERE_LAMBDA, TROPOSPHERE_INITIAL_PRESSURE, TROPOSPHERE_INITIAL_DENSITY, \
    TROPOSPHERE_FINAL_HEIGHT
from ..utils.environment_constants import LOW_STRATOSPHERE_INITIAL_TEMPERATURE, \
    LOW_STRATOSPHERE_INITIAL_PRESSURE, LOW_STRATOSPHERE_INITIAL_DENSITY
from ..utils.environment_constants import HEIGHT_STRATOSPHERE_LAMBDA, \
    HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE, HEIGHT_STRATOSPHERE_INITIAL_PRESSURE, \
    HEIGHT_STRATOSPHERE_INITIAL_DENSITY, HEIGHT_STRATOSPHERE_INITIAL_HEIGHT
from ..utils.environment_constants import DYNAMIC_VISCOSITY_ARRAY, ALTITUDE_VISCOSITY_ARRAY


@dataclass
class AirPropertiesModel:
    altitude_ref: float = 0

    def getCorrectAltitude(self, altitude_agl: float):
        return self.altitude_ref + altitude_agl

    def getAtmosphereZone(self, altitude_agl: float) -> AtmosphereZone:
        return AtmosphereZone.getZone(altitude=self.getCorrectAltitude(altitude_agl=altitude_agl))

    def getViscosity(self, altitude_agl: float) -> float:
        interpolation_function = interp1d(ALTITUDE_VISCOSITY_ARRAY, DYNAMIC_VISCOSITY_ARRAY, kind='cubic')
        return interpolation_function(self.getCorrectAltitude(altitude_agl=altitude_agl)) * 1e-5

    def getGravity(self, altitude_agl: float) -> float:
        return GRAVITY_ACCELERATION * ((EARTH_RADIUS / (EARTH_RADIUS + self.getCorrectAltitude(altitude_agl=altitude_agl))) ** 2)

    def getTemperature(self, altitude_agl: float) -> float:

        zone: AtmosphereZone = self.getAtmosphereZone(altitude_agl=altitude_agl)

        if zone == AtmosphereZone.TROPOSPHERE:  # Troposphere
            return TROPOSPHERE_INITIAL_TEMPERATURE + TROPOSPHERE_LAMBDA * self.getCorrectAltitude(altitude_agl=altitude_agl)

        if zone == AtmosphereZone.LOW_STRATOSPHERE:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_TEMPERATURE

        if zone == AtmosphereZone.HEIGHT_STRATOSPHERE:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE + HEIGHT_STRATOSPHERE_LAMBDA * (
                        self.getCorrectAltitude(altitude_agl=altitude_agl) - HEIGHT_STRATOSPHERE_INITIAL_HEIGHT)

        return 0.0

    def getPressure(self, altitude_agl: float) -> float:

        zone: AtmosphereZone = self.getAtmosphereZone(altitude_agl=altitude_agl)

        if zone == AtmosphereZone.TROPOSPHERE:  # Troposphere
            return TROPOSPHERE_INITIAL_PRESSURE * pow(self.getTemperature(altitude_agl) / TROPOSPHERE_INITIAL_TEMPERATURE,
                                                      - self.getGravity(altitude_agl=altitude_agl) / (AIR_GAS_CONSTANT * TROPOSPHERE_LAMBDA))

        if zone == AtmosphereZone.LOW_STRATOSPHERE:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_PRESSURE * math.exp(
                - self.getGravity(altitude_agl=altitude_agl) * (self.getCorrectAltitude(altitude_agl=altitude_agl) - TROPOSPHERE_FINAL_HEIGHT) / (
                            AIR_GAS_CONSTANT * TROPOSPHERE_INITIAL_TEMPERATURE))

        if zone == AtmosphereZone.HEIGHT_STRATOSPHERE:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_PRESSURE * pow(
                self.getTemperature(altitude_agl) / HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE,
                - self.getGravity(altitude_agl=altitude_agl) / (AIR_GAS_CONSTANT * HEIGHT_STRATOSPHERE_LAMBDA))

        return 0.0

    def getDensity(self, altitude_agl: float) -> float:

        zone: AtmosphereZone = self.getAtmosphereZone(altitude_agl=altitude_agl)

        if zone == AtmosphereZone.TROPOSPHERE:  # Troposphere
            return TROPOSPHERE_INITIAL_DENSITY * pow(self.getTemperature(altitude_agl) / TROPOSPHERE_INITIAL_TEMPERATURE,
                                                     - (1 + self.getGravity(altitude_agl=altitude_agl) / (
                                                                 AIR_GAS_CONSTANT * TROPOSPHERE_LAMBDA)))

        if zone == AtmosphereZone.LOW_STRATOSPHERE:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_DENSITY * math.exp(
                - self.getGravity(altitude_agl=altitude_agl) * (self.getCorrectAltitude(altitude_agl=altitude_agl) - 11000) / (AIR_GAS_CONSTANT * LOW_STRATOSPHERE_INITIAL_TEMPERATURE))

        if zone == AtmosphereZone.HEIGHT_STRATOSPHERE:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_DENSITY * pow(
                self.getTemperature(altitude_agl) / HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE,
                1 - self.getGravity(altitude_agl=altitude_agl) / (AIR_GAS_CONSTANT * HEIGHT_STRATOSPHERE_LAMBDA))

        return 0.0

    def getSoundSpeed(self, altitude_agl: float) -> float:
        return math.sqrt(AIR_GAMMA * AIR_GAS_CONSTANT * self.getTemperature(altitude_agl=altitude_agl))
