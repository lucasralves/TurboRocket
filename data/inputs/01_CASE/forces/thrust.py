from core.utils.math.models.vector_model import Vector

# Inputs
# time - seconds
def booster(time: float) -> float:  # [force]
    BOOSTER_MEAN_THRUST: float = 600  # [N]
    BOOSTER_BURN_TIME: float = 0.2  # [sec]
    if time > BOOSTER_BURN_TIME:
        return 0.0
    return BOOSTER_MEAN_THRUST


# ----------------------------------------------------------------------------#

# Inputs
# mach - Mach Number
# altitude - rocket altitude
def turbojet(mach: float, altitude: float) -> float:  # [force]
    if altitude < 500:
        return 300
    else:
        return 0


# ----------------------------------------------------------------------------#

# Inputs
# time - seconds
# mach - Mach Number
# altitude - rocket altitude
def value(mach: float, altitude: float, time: float, atitude: Vector) -> Vector:
    return atitude.unary().multiply(scalar=booster(time=time) + turbojet(mach=mach, altitude=altitude))
