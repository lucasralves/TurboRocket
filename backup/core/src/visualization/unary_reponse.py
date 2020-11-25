import os
from typing import List
import math

def create_images_directory(path: str) -> None:
    os.mkdir(path + '/images3D')
    os.mkdir(path + '/images2D')

def cross_product(a: List[float], b: List[float]) -> List[float]:
    return [a[1] * b[2] - a[2] * b[1], a[0] * b[2] - a[2] * b[0], a[0] * b[1] - a[1] * b[0]]

def dot_product(a: List[float], b: List[float]) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def vector_norm(a: List[float]) -> float:
    return math.sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2])

def angle_between_vectors(a: List[float], b: List[float]) -> float:
    return math.atan(vector_norm(cross_product(a, b)) / dot_product(a, b))

def solve(cm: float, cmd: float, speed: float, wind: float, time: float, max_time: float):

    # Instant parameters
    x0: List[float] = [1.0, 0.0, 0.0]
    y0: List[float] = [0.0, 1.0, 0.0]
    z0: List[float] = [0.0, 0.0, 1.0]

    # Parameters to save
    x_out: List[List[float]] = []
    y_out: List[List[float]] = []
    z_out: List[List[float]] = []
    time_out: List[float] = []
    attack_angle_out: List[float] = []

    # Counter
    i = 0

    M: List[float]

    while max_time < time_out[i]:
        # Attack angle
        attack_angle_out.append(angle_between_vectors(z0, [0.0, wind, speed]))

        # Moment
        aux = cross_product(z0, [0.0, wind, speed])
        scalar = 0.5 * 1.225 * 1 * speed * speed * 1 / vector_norm(aux)
        M = 0.0

        # Angular acceleration

        # Integrate