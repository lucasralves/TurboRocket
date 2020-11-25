# Python packages
from typing import List
import math

# Models
from core.models.simulation.data import Data
from core.models.simulation.flight_stage import FlightStage
from core.models.simulation.input_model import InputModel

# Math
from core.math.utils import multiplyVector, addVectors, unaryVector, normVector

# Forces
from engine import thrust

#---------------------------------------------------------------------#
class Acceleration:

    def __init__(self, initial_conditions: InputModel, launch_rail_length: float):
        self.stage = FlightStage.BASE
        self.initial_conditions = initial_conditions
        self.launch_rail_length = launch_rail_length

    def value(self, data: Data) -> List[float]:

        total_force: List[float] = [0, 0, 0]

        if self.stage == FlightStage.BASE:

            total_force = addVectors(
                a=self.drag(
                    vx=data.velocity.x,
                    vy=data.velocity.y,
                    vz=data.velocity.z,
                ),
                b=addVectors(
                    a=self.engine(altitude=data.position.z, time=data.time),
                    b=self.weight()
                )
            )

            self.setFlightStage(data=data, total_force=total_force)

            if total_force[2] < 0:
                return [0, 0, 0]
            else:
                return multiplyVector(vector=total_force, scalar=1/10)

        elif self.stage == FlightStage.LAUNCH_RAIL:

            total_force = addVectors(
                a=self.drag(
                    vx=data.velocity.x,
                    vy=data.velocity.y,
                    vz=data.velocity.z,
                ),
                b=addVectors(
                    a=self.engine(altitude=data.position.z, time=data.time),
                    b=self.weight()
                )
            )

            self.setFlightStage(data=data, total_force=total_force)

            return multiplyVector(vector=total_force, scalar=1 / 10)

        elif self.stage == FlightStage.PROPELLED:

            total_force = addVectors(
                a=self.drag(
                    vx=data.velocity.x,
                    vy=data.velocity.y,
                    vz=data.velocity.z,
                ),
                b=addVectors(
                    a=self.engine(altitude=data.position.z, time=data.time),
                    b=self.weight()
                )
            )

            self.setFlightStage(data=data, total_force=total_force)

            return multiplyVector(vector=total_force, scalar=1 / 10)

        elif self.stage == FlightStage.BALLISTIC:

            total_force = addVectors(
                a=self.drag(
                    vx=data.velocity.x,
                    vy=data.velocity.y,
                    vz=data.velocity.z,
                ),
                b=self.weight()
            )

            self.setFlightStage(data=data, total_force=total_force)

            return multiplyVector(vector=total_force, scalar=1 / 10)

        elif self.stage == FlightStage.PARACHUTE:

            total_force = addVectors(
                a=self.parachute(
                    vx=data.velocity.x,
                    vy=data.velocity.y,
                    vz=data.velocity.z,
                    z=data.position.z
                ),
                b=self.weight()
            )

            return total_force

        return total_force

    @staticmethod
    def drag(vx: float, vy: float, vz: float) -> List[float]:
        D = 0.5 * 1.225 * (vx ** 2 + vy ** 2 + vz ** 2) * 1 * 0.14
        return multiplyVector(
            vector=unaryVector(a=[-vx, -vy, -vz]),
            scalar=D
        )

    @staticmethod
    def launchRail() -> List[float]:
        return [0, 0, 0]

    @staticmethod
    def normalForce() -> List[float]:
        return [0, 0, 0]

    @staticmethod
    def engine(altitude: float, time: float) -> List[float]:
        return [0, 0, thrust(altitude=altitude, mach=0, time=time)]

    @staticmethod
    def weight() -> List[float]:
        return [0, 0, - 100]

    @staticmethod
    def parachute(vx: float, vy: float, vz: float, z: float) -> List[float]:
        if z < 420:
            D = 0.5 * 1.225 * (vx ** 2 + vy ** 2 + vz ** 2) * 1 * 2.2
        else:
            D = 0.5 * 1.225 * (vx ** 2 + vy ** 2 + vz ** 2) * 1 * 1.2
        return multiplyVector(
            vector=unaryVector(a=[-vx, -vy, -vz]),
            scalar=D
        )

    def setFlightStage(self, data: Data, total_force: List[float]) -> None:
        if self.stage == FlightStage.BASE:

            if total_force[2] > 0:
                self.stage = FlightStage.LAUNCH_RAIL

        elif self.stage == FlightStage.LAUNCH_RAIL:

            if data.position.z > self.launch_rail_length:
                self.stage = FlightStage.PROPELLED

        elif self.stage == FlightStage.PROPELLED:

            if normVector(a=self.engine(altitude=data.position.z, time=data.time)) < 1e-6:
                self.stage = FlightStage.BALLISTIC

        elif self.stage == FlightStage.BALLISTIC:

            if data.velocity.z < 1e-6:
                self.stage = FlightStage.PARACHUTE

