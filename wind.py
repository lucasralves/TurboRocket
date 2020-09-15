# WIND INPUT
# The output of the wind_settings method is a float number corresponding
# to the wind speed in the simulation

########################################################################
# Python libraries
from typing import List

# Simulation settings
from core.simulation.wind_settings import WindSettings

########################################################################
# WIND MODEL
# Constant - const
# Power - pow
# Logarithmic - log

WIND_REF_SPEED = 10                 # const | pow | log
WIND_REF_HEIGHT = 1                 # pow | log
WIND_REF_EXPONENT = 0.14            # pow
WIND_REF_PLANE_DISPLACEMENT = 10    # log
WIND_REF_SURFACE_ROUGHNESS = 0.1    # log
########################################################################

# Class
windModel = WindSettings(
    speed_ref=WIND_REF_SPEED,
    height_ref=WIND_REF_HEIGHT,
    exponent=WIND_REF_EXPONENT,
    plane_displacement=WIND_REF_PLANE_DISPLACEMENT,
    surface_roughness=WIND_REF_SURFACE_ROUGHNESS)

# Inputs
# time - seconds
# altitude - meters
# Output
# speed - meters per second
def wind_settings(time: float, altitude: float) -> List[float]:
    return 0

