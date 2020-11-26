from typing import List
import math

ZERO_DIVISION: float = 1e-8

def dotProduct(a: List[float], b: List[float]) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def multiplyVector(vector: List[float], scalar: float) -> List[float]:
    return [vector[0] * scalar, vector[1] * scalar, vector[2] * scalar]

def addVectors(a: List[float], b: List[float]) -> List[float]:
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def normVector(a: List[float]) -> float:
    return math.sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)

def unaryVector(a: List[float]) -> List[float]:
    if normVector(a=a) < ZERO_DIVISION:
        return [0, 0, 0]
    else:
        return multiplyVector(vector=a, scalar=1 / normVector(a=a))