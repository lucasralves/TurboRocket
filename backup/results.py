# This file sets the outputs that will be exported to the results folder

###############################################################
# 00_OVERVIEW
UNARY_RESPONSE = True

###############################################################
# 01_SIMULATION FOLDER
FLIGHT_DETAILS_FILE = True

# 01_PERFORMANCE SUBFOLDER
TRAJECTORY_FIG = True
VELOCITY_FIG = True
ACCELERATION_FIG = True
VERTICAL_ANGLE_FIG = True
TURBOJET_THRUST_FIG = True
BOOSTERS_THRUST_FIG = True

# 02_AERODYNAMIC_PARAMETERS SUBFOLDER
REYNOLDS_FIG = True
MACH_FIG = True
DYNAMIC_PRESSURE_FIG = True
DRAG_COEFFICIENT_FIG = True
NORMAL_FORCE_FIG = False
MOMENT_FIG = False
DAMPING_MOMENT_FIG = False
DRAG_FIG = False

# 03_CONTROLLER SUBFOLDER
ENGINE_ANGLE_FIG = True
CONTROLLER_MOMENT_FIG = True

###############################################################
# 02_ENVIRONMENT SUBFOLDER
TEMPERATURE_FIG = True
PRESSURE_FIG = True
DENSITY_FIG = True
VISCOSITY_FIG = True
WIND_FIG = True