from core.utils.math.models.vector_model import Vector
from settings import CD_VERTICAL_FIRST_PARACHUTE, REFERENCE_AREA_FIRST_PARACHUTE
from settings import CD_VERTICAL_SECOND_PARACHUTE, REFERENCE_AREA_SECOND_PARACHUTE, SECOND_PARACHUTE_OPENING_HEIGHT

def value(altitude: float, velocity: Vector, rho: float) -> Vector:
    if velocity.z < 0 and altitude > SECOND_PARACHUTE_OPENING_HEIGHT:  # First parachute
        return velocity.unary().multiply(scalar=- 0.5 * rho * (velocity.norm() ** 2) * REFERENCE_AREA_FIRST_PARACHUTE * CD_VERTICAL_FIRST_PARACHUTE)
    else:
        return velocity.unary().multiply(scalar=- 0.5 * rho * (velocity.norm() ** 2) * REFERENCE_AREA_SECOND_PARACHUTE * CD_VERTICAL_SECOND_PARACHUTE)