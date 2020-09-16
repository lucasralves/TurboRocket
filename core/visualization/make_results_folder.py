# Python packages
import os

# Results
from results import TEMPERATURE_FIG, PRESSURE_FIG, DENSITY_FIG, VISCOSITY_FIG, WIND_FIG, ENGINE_ANGLE_FIG, \
    CONTROLLER_MOMENT_FIG, DRAG_FIG, DAMPING_MOMENT_FIG, MOMENT_FIG, NORMAL_FORCE_FIG, DRAG_COEFFICIENT_FIG, \
    DYNAMIC_PRESSURE_FIG, MACH_FIG, REYNOLDS_FIG, BOOSTERS_THRUST_FIG, TURBOJET_THRUST_FIG, VERTICAL_ANGLE_FIG, \
    ACCELERATION_FIG, VELOCITY_FIG, TRAJECTORY_FIG

# Number of simulations cases
def number_of_simulations_cases() -> int:
    folder_count = 0
    input_path = "results"
    for folders in os.listdir(input_path):
        folder_count += 1
    return folder_count

# New case name
def get_new_case_name() -> str:
    directory_number = number_of_simulations_cases()
    if directory_number > 10:
        path = 'results/' + str(directory_number) + '_CASE'
    else:
        path = 'results/' + '0' + str(directory_number) + '_CASE'
    return path

##########################################################################
def environment_check(path: str):
    if TEMPERATURE_FIG or PRESSURE_FIG or DENSITY_FIG or VISCOSITY_FIG or WIND_FIG:
        path = path + '/02_ENVIRONMENT'
        os.mkdir(path)

def controller_check(path: str):
    if ENGINE_ANGLE_FIG or CONTROLLER_MOMENT_FIG:
        path = path + '/01_SIMULATION/03_CONTROLLER'
        os.mkdir(path)

def aerodynamic_check(path: str):
    if REYNOLDS_FIG or MACH_FIG or DYNAMIC_PRESSURE_FIG or DRAG_COEFFICIENT_FIG or NORMAL_FORCE_FIG or MOMENT_FIG or DAMPING_MOMENT_FIG or DRAG_FIG:
        path = path + '/01_SIMULATION/02_AERODYNAMIC_PARAMETERS'
        os.mkdir(path)

def performance_check(path: str):
    if TRAJECTORY_FIG or VELOCITY_FIG or ACCELERATION_FIG or VERTICAL_ANGLE_FIG or TURBOJET_THRUST_FIG or BOOSTERS_THRUST_FIG:
        path = path + '/01_SIMULATION/01_PERFORMANCE'
        os.mkdir(path)

# Create folders
def create_simulation_case() -> str:
    # Create results folder
    if os.path.exists('results') is False:
        os.mkdir('results')

    # Get correct path to case folder and create it
    path = get_new_case_name()
    os.mkdir(path)

    # Simulation folder
    os.mkdir(path + '/01_SIMULATION')
    with open(path + '/01_SIMULATION/flight_overview.out', 'w') as fp:
        pass
    controller_check(path)
    aerodynamic_check(path)
    performance_check(path)

    # Environment folder
    environment_check(path)

    return path