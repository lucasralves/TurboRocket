# Air
AIR_GAS_CONSTANT = 287.54
AIR_GAMMA = 1.4

# Gravity
GRAVITY_ACCELERATION = 9.8
EARTH_RADIUS = 6371000

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