from core.utils.math.models.vector_model import Vector

def value(rho: float, area: float, velocity: Vector, cd: float) -> Vector:
    return velocity.unary().multiply(scalar=- 0.5 * rho * (velocity.norm() ** 2) * area * cd)