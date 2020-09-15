# 1) This class calculates the temperature, pressure and density according to
# the International Standard Atmosphere
# 2) The viscosity is calculated as a function of temperature

##############################################################################
# Python Packages
import math
from scipy.interpolate import interp1d

##############################################################################
# Constants

GRAVITY_ACCELERATION = 9.8
AIR_GAS_CONSTANT = 287.54

# Troposphere
TROPOSPHERE_INITIAL_HEIGHT = 0.0
TROPOSPHERE_FINAL_HEIGHT = 11000
TROPOSPHERE_INITIAL_TEMPERATURE = 288
TROPOSPHERE_LAMBDA = -6.5 * 1e-3
TROPOSPHERE_INITIAL_PRESSURE = 101325
TROPOSPHERE_INITIAL_DENSITY = 1.225

# Low Stratosphere
LOW_STRATOSPHERE_INITIAL_HEIGHT = 11000
LOW_STRATOSPHERE_FINAL_HEIGHT = 25000
LOW_STRATOSPHERE_INITIAL_TEMPERATURE = 216.5
LOW_STRATOSPHERE_INITIAL_PRESSURE = 22552
LOW_STRATOSPHERE_INITIAL_DENSITY = 0.3629

# Height Stratosphere
HEIGHT_STRATOSPHERE_INITIAL_HEIGHT = 25000
HEIGHT_STRATOSPHERE_FINAL_HEIGHT = 47000
HEIGHT_STRATOSPHERE_LAMBDA = 0.003
HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE = LOW_STRATOSPHERE_INITIAL_TEMPERATURE
HEIGHT_STRATOSPHERE_INITIAL_PRESSURE = 2481
HEIGHT_STRATOSPHERE_INITIAL_DENSITY = 0.0399

# Viscosity array
DYNAMIC_VISCOSITY_ARRAY = [1.821, 1.789, 1.758, 1.726, 1.694, 1.661, 1.628, 1.595, 1.561, 1.527, 1.493, 1.458, 1.422,
                           1.422, 1.448, 1.475, 1.601, 1.704, 1.584, 1.438, 1.321]
ALTITUDE_VISCOSITY_ARRAY = [-1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000,
                            30000, 40000, 50000, 60000, 70000, 80000]


class EnvironmentSettings:
    altitude_ref: float = 0

    def __init__(self, altitude_ref: float = 0):
        self.altitude_ref = altitude_ref

    def getTemperature(self, altitude: float) -> float:
        if altitude < TROPOSPHERE_FINAL_HEIGHT:  # Troposphere
            return TROPOSPHERE_INITIAL_TEMPERATURE + TROPOSPHERE_LAMBDA * altitude
        elif TROPOSPHERE_FINAL_HEIGHT <= altitude < LOW_STRATOSPHERE_FINAL_HEIGHT:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_TEMPERATURE
        elif HEIGHT_STRATOSPHERE_INITIAL_HEIGHT <= altitude < HEIGHT_STRATOSPHERE_FINAL_HEIGHT:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE + HEIGHT_STRATOSPHERE_LAMBDA * (
                    altitude - HEIGHT_STRATOSPHERE_INITIAL_HEIGHT)
        return 0.0

    def getPressure(self, altitude: float) -> float:
        if altitude < TROPOSPHERE_FINAL_HEIGHT:  # Troposphere
            return TROPOSPHERE_INITIAL_PRESSURE * pow(self.getTemperature(altitude) / TROPOSPHERE_INITIAL_TEMPERATURE,
                                                      - GRAVITY_ACCELERATION / (AIR_GAS_CONSTANT * TROPOSPHERE_LAMBDA))
        elif TROPOSPHERE_FINAL_HEIGHT <= altitude < LOW_STRATOSPHERE_FINAL_HEIGHT:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_PRESSURE * math.exp(
                - GRAVITY_ACCELERATION * (altitude - TROPOSPHERE_FINAL_HEIGHT) / (
                        AIR_GAS_CONSTANT * TROPOSPHERE_INITIAL_TEMPERATURE))
        elif HEIGHT_STRATOSPHERE_INITIAL_HEIGHT <= altitude < HEIGHT_STRATOSPHERE_FINAL_HEIGHT:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_PRESSURE * pow(
                self.getTemperature(altitude) / HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE,
                - GRAVITY_ACCELERATION / (AIR_GAS_CONSTANT * HEIGHT_STRATOSPHERE_LAMBDA))
        return 0.0

    def getDensity(self, altitude: float) -> float:
        if altitude < TROPOSPHERE_FINAL_HEIGHT:  # Troposphere
            return TROPOSPHERE_INITIAL_DENSITY * pow(self.getTemperature(altitude) / TROPOSPHERE_INITIAL_TEMPERATURE,
                                                     - (1 + GRAVITY_ACCELERATION / (
                                                             AIR_GAS_CONSTANT * TROPOSPHERE_LAMBDA)))
        elif TROPOSPHERE_FINAL_HEIGHT <= altitude < LOW_STRATOSPHERE_FINAL_HEIGHT:  # Low Stratosphere
            return LOW_STRATOSPHERE_INITIAL_DENSITY * math.exp(
                - GRAVITY_ACCELERATION * (altitude - 11000) / (AIR_GAS_CONSTANT * LOW_STRATOSPHERE_INITIAL_TEMPERATURE))
        elif HEIGHT_STRATOSPHERE_INITIAL_HEIGHT <= altitude < HEIGHT_STRATOSPHERE_FINAL_HEIGHT:  # Height Stratosphere
            return HEIGHT_STRATOSPHERE_INITIAL_DENSITY * pow(
                self.getTemperature(altitude) / HEIGHT_STRATOSPHERE_INITIAL_TEMPERATURE,
                1 - GRAVITY_ACCELERATION / (AIR_GAS_CONSTANT * HEIGHT_STRATOSPHERE_LAMBDA))
        return 0.0

    def getViscosity(self, altitude: float) -> float:
        interpolation_function = interp1d(ALTITUDE_VISCOSITY_ARRAY, DYNAMIC_VISCOSITY_ARRAY, kind='cubic')
        return interpolation_function(altitude) * 1e-5
