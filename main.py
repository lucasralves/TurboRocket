import core.solve as solve

# ROCKET SIMULATION INTERFACE

# Scripts
# wind.py - wind model implementation
# rocket.py - rocket geometry implementation

# Initial parameters
# LAUNCH_ALTITUDE: initial altitude in km [ASL]
# LAUNCH_ANGLE: initial launch angle in degrees [between vertical axis and rocket longitudinal axis]

####################################################################################################
# Packages
import core.solve

####################################################################################################
# Parameters
LAUNCH_ALTITUDE: float = 0
LAUNCH_ANGLE: float = 0

# Solve
solve.run()
