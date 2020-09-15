import core.solve as solve

# ROCKET SIMULATION INTERFACE

# Scripts
# wind.py - wind model implementation
# rocket.py - rocket geometry implementation

# Initial parameters
# LAUNCH_ALTITUDE: initial altitude in km [ASL]
# LAUNCH_ANGLE: initial launch angle in degrees [between vertical axis and rocket longitudinal axis]

####################################################################################################
# Parameters
from core.models.geometry.body_model import BodyModel
from core.models.geometry.fin_model import FinModel
from core.models.geometry.nose_model import NoseModel
from core.models.geometry.transition_model import TransitionModel

LAUNCH_ALTITUDE: float = 0
LAUNCH_ANGLE: float = 0

# Files
import rocket
import wind

from core.simulation.wind_settings import WindSettings

w = WindSettings()

print(w.logarithmicModel(0))


# Solution
#solve.simulate(rocket, wind, LAUNCH_ANGLE, LAUNCH_ALTITUDE)
