# ROCKET SIMULATION INTERFACE

# This file has the inputs necessary to simulate the rocket flight

# Scripts
# wind.py - wind implementation
# rocket.py - rocket geometry
# thrust.py - engine thrust implementation
# control.py - thrust vectoring control parameters


# Simulation parameters
# LAUNCH_ALTITUDE: initial altitude in km [ASL]
# LAUNCH_RAIL_LENGTH:
# LAUNCH_RAIL_ANGLE: initial launch angle in degrees [between vertical axis and rocket longitudinal axis]

####################################################################################################
# Packages

# Solve
from core.modules.simulation.solve import solve

# Models
from core.utils.math.models.vector_model import Vector
from core.modules.simulation.models.input_model import Input, Forces, InitialCondition
import forces

# Rocket
import rocket

####################################################################################################
# Inputs
inputs = Input(
    # Forces
    forces=Forces(
        weight=forces.weight,
        thrust=forces.thrust,
        drag=forces.drag,
        parachute_drag=forces.parachute_drag
    ),
    # Initial Conditions
    initial_condition=InitialCondition(
        velocity=Vector(x=0, y=0, z=0),
        position=Vector(x=0, y=0, z=0),
        atitude=Vector(x=0, y=0, z=1)
    ),
    # Rocket
    rocket=rocket.getRocket(),
    # Launch Rail Length
    launch_rail_length=10
)

# Solve
solve(y0=inputs)