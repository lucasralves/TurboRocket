# Python packages
from typing import List
import scipy.integrate as ode
from time import time

# Models
from core.modules.simulation.models.data import Data
from core.utils.math.models.vector_model import Vector
from core.modules.simulation.models.output_model import OutputModel
from core.modules.simulation.models.input_model import Input

# Acceleration
from core.modules.simulation.acceleration import Acceleration

# Visualization
from core.modules.handling_data.terminal import printData, printHeader
from core.modules.handling_data.plot import makePlots

# Settings
from settings import MAX_TIME_STEP, PRINT_INTERVAL, MAX_SIMULATION_TIME

# -------------------------------------------------------------------------------#
# Solve
def solve(y0: Input):

    # Derivative equations
    # Inputs
    # t: time
    # y: [
    #       position_x,
    #       position_y,
    #       position_z,
    #       velocity_x,
    #       velocity_y,
    #       velocity_z
    # ]
    def derivative(t, y) -> List[float]:  # t: float, y: List[float]

        # Create data model
        data_der = Data(position=Vector(x=y[0], y=y[1], z=y[2]), velocity=Vector(x=y[3], y=y[4], z=y[5]), time=t)

        y_dot = [0] * len(y)

        # Velocity
        y_dot[0], y_dot[1], y_dot[2] = y[3], y[4], y[5]

        # Acceleration
        y_dot[3], y_dot[4], y_dot[5] = acceleration.value(data=data_der)

        return y_dot

    print('\n01 - Simulation Initialized\n')

    # Initial simulation time
    start_time = time()

    # Create class
    acceleration = Acceleration(inputs=y0)

    # Initial conditions
    output = OutputModel(
        position=[y0.initial_condition.position],
        velocity=[y0.initial_condition.position],
        time=[0.0],
    )

    # Solve
    solution = ode.RK45(derivative, t0=0.0, y0=y0.initial_condition.toList(), t_bound=MAX_SIMULATION_TIME, max_step=MAX_TIME_STEP)
    print_data = 0
    data = Data(position=Vector(x=0.0, y=0.0, z=0.0), velocity=Vector(x=0.0, y=0.0, z=0.0), time=0.0)
    printHeader()
    while True:
        solution.step()
        output.insertFromList(t=solution.t, y=solution.y)
        if output.position[len(output.position) - 1].z <= 0.0:
            data.updateFromList(t=solution.t, y=solution.y)
            printData(data=data)
            break
        if solution.t - print_data >= PRINT_INTERVAL or print_data == 0:
            print_data = solution.t + PRINT_INTERVAL
            data.updateFromList(t=solution.t, y=solution.y)
            printData(data=data)

    # End simulation time
    end_time = time()

    print('\n   Simulation ended in %.4f seconds' % (end_time - start_time))

    print('\n04 - Generating Log')

    print('\n05 - Generating Plots')
    makePlots(output=output)

    print('\n06 - Generating Report')

