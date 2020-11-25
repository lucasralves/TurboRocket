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
from models.enum.atmosphere_zone import AtmosphereZone

# Constants
from environment_constants import AIR_GAS_CONSTANT
from environment_constants import GRAVITY_ACCELERATION

##############################################################################

# Troposphere
TROPOSPHERE_INITIAL_TEMPERATURE = 288
TROPOSPHERE_LAMBDA = -6.5 * 1e-3
TROPOSPHERE_INITIAL_PRESSURE = 101325
TROPOSPHERE_INITIAL_DENSITY = 1.225

# Low Stratosphere
LOW_STRATOSPHERE_INITIAL_TEMPERATURE = 216.5
LOW_STRATOSPHERE_INITIAL_PRESSURE = 22552
LOW_STRATOSPHERE_INITIAL_DENSITY = 0.3629

# Height Stratosphere
HEIGHT_STRATOSPHERE_LAMBDA = 0.003
HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE = LOW_STRATOSPHERE_INITIAL_TEMPERATURE
HEIGHT_STRATOSPHERE_INITIAL_PRESSURE = 2481
HEIGHT_STRATOSPHERE_INITIAL_DENSITY = 0.0399

# Viscosity array
DYNAMIC_VISCOSITY_ARRAY = [1.821, 1.789, 1.758, 1.726, 1.694, 1.661, 1.628, 1.595, 1.561, 1.527, 1.493, 1.458, 1.422,
                           1.422, 1.448, 1.475, 1.601, 1.704, 1.584, 1.438, 1.321]
ALTITUDE_VISCOSITY_ARRAY = [-1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000,
                            30000, 40000, 50000, 60000, 70000, 80000]

@dataclass
class EnvironmentSettings:

    altitude_ref: float = 0

    @staticmethod
    def getAtmosphereZone(altitude: float) -> AtmosphereZone:
        return AtmosphereZone.getZone(altitude=altitude)

    @staticmethod
    def getViscosity(altitude: float) -> float:
        interpolation_function = interp1d(ALTITUDE_VISCOSITY_ARRAY, DYNAMIC_VISCOSITY_ARRAY, kind='cubic')
        return interpolation_function(altitude) * 1e-5

    @classmethod
    def getTemperature(self, altitude: float) -> float:

        zone: AtmosphereZone = self.getAtmosphereZone(altitude=altitude)

        if zone == AtmosphereZone.TROPOSPHERE:  # Troposphere
            return TROPOSPHERE_INITIAL_TEMPERATURE + TROPOSPHERE_LAMBDA * altitude

        if zone == AtmosphereZone.LOW_STRATOSPHERE:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_TEMPERATURE

        if zone == AtmosphereZone.HEIGHT_STRATOSPHERE:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE + HEIGHT_STRATOSPHERE_LAMBDA * (altitude - HEIGHT_STRATOSPHERE_INITIAL_HEIGHT)
        
        return 0.0

    @classmethod
    def getPressure(self, altitude: float) -> float:

        zone: AtmosphereZone = self.getAtmosphereZone(altitude=altitude)

        if zone == AtmosphereZone.TROPOSPHERE:  # Troposphere
            return TROPOSPHERE_INITIAL_PRESSURE * pow(self.getTemperature(altitude) / TROPOSPHERE_INITIAL_TEMPERATURE, - GRAVITY_ACCELERATION / (AIR_GAS_CONSTANT * TROPOSPHERE_LAMBDA))
        
        if zone == AtmosphereZone.LOW_STRATOSPHERE:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_PRESSURE * math.exp(- GRAVITY_ACCELERATION * (altitude - TROPOSPHERE_FINAL_HEIGHT) / (AIR_GAS_CONSTANT * TROPOSPHERE_INITIAL_TEMPERATURE))
        
        if zone == AtmosphereZone.HEIGHT_STRATOSPHERE:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_PRESSURE * pow(self.getTemperature(altitude) / HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE, - GRAVITY_ACCELERATION / (AIR_GAS_CONSTANT * HEIGHT_STRATOSPHERE_LAMBDA))
        
        return 0.0

    @classmethod
    def getDensity(self, altitude: float) -> float:

        zone: AtmosphereZone = self.getAtmosphereZone(altitude=altitude)

        if zone == AtmosphereZone.TROPOSPHERE:  # Troposphere
            return TROPOSPHERE_INITIAL_DENSITY * pow(self.getTemperature(altitude) / TROPOSPHERE_INITIAL_TEMPERATURE, - (1 + GRAVITY_ACCELERATION / (AIR_GAS_CONSTANT * TROPOSPHERE_LAMBDA)))
        
        if zone == AtmosphereZone.LOW_STRATOSPHERE:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_DENSITY * math.exp(- GRAVITY_ACCELERATION * (altitude - 11000) / (AIR_GAS_CONSTANT * LOW_STRATOSPHERE_INITIAL_TEMPERATURE))
        
        if zone == AtmosphereZone.HEIGHT_STRATOSPHERE:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_DENSITY * pow(self.getTemperature(altitude) / HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE, 1 - GRAVITY_ACCELERATION / (AIR_GAS_CONSTANT * HEIGHT_STRATOSPHERE_LAMBDA))
        
        return 0.0
