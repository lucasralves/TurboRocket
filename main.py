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
LAUNCH_ALTITUDE: float = 0
LAUNCH_ANGLE: float = 0

# Files
import rocket
import wind

# Solution
#solve.simulate(rocket, wind, LAUNCH_ANGLE, LAUNCH_ALTITUDE)
