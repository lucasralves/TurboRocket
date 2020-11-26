from core.utils.math.models.vector_model import Vector

def value(mass: float, g: float) -> Vector:
    return Vector(
        x=0,
        y=0,
        z=- mass * g
    )
