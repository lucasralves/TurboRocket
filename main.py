# ROCKET SIMULATION INTERFACE

# This file has the inputs necessary to simulate the rocket flight

# Scripts
# wind.py - wind implementation
# rocket.py - rocket geometry
# engine.py - engine thrust implementation
# control.py - thrust vectoring control parameters


# Simulation parameters
# LAUNCH_ALTITUDE: initial altitude in km [ASL]
# LAUNCH_RAIL_LENGTH:
# LAUNCH_RAIL_ANGLE: initial launch angle in degrees [between vertical axis and rocket longitudinal axis]

####################################################################################################
# Packages

# Solve
from core.simulation.solve import solve

# Models
from core.models.simulation.input_model import InputModel
from core.models.math.vector_model import Vector

####################################################################################################
# Inputs

# Rocket
import rocket

# Launch
LAUNCH_RAIL_LENGTH = 10

# Environment


# Forces

# Initial conditions
initial_condition = InputModel(
    position=Vector(x=0, y=0, z=0),
    velocity=Vector(x=0, y=0, z=0),
    altitude=0.0
)

# Solve
solve(y0=initial_condition, launch_rail_length=LAUNCH_RAIL_LENGTH)