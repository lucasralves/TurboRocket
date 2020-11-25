from dataclasses import dataclass

@dataclass
class Vector:
    x: float = 0
    y: float = 0
    z: float = 0

@dataclass
class Axis:
    x_unit: Vector
    y_unit: Vector
    z_unit: Vector

@dataclass
class Translation:
    acceleration: Vector
    velocity: Vector
    position: Vector

@dataclass
class Quaternion:
    scalar: float
    vector: Vector

@dataclass
class Rotation:
    acceleration: Vector
    velocity: Vector
    atitude: Axis
    quaternion: Quaternion

@dataclass
class FMParameter:
    inertial: Vector
    rocket: Vector
    norm: float

@dataclass
class Forces:
    engine: FMParameter
    drag: FMParameter
    normal_force: FMParameter

@dataclass
class OutputModel:
    time: float
    translation: Translation
    rotation: Rotation
