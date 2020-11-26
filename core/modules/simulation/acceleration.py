# Models
from core.modules.simulation.models.data import Data
from core.modules.simulation.enums.flight_stage import FlightStage
from core.modules.simulation.models.input_model import Input
from core.utils.math.models.vector_model import Vector

# Settings
from settings import ROCKET_MASS

#---------------------------------------------------------------------#
class Acceleration:

    def __init__(self, inputs: Input):
        self.stage = FlightStage.BASE
        self.inputs = inputs

    def value(self, data: Data) -> Vector:

        total_force: Vector = Vector(x=0, y=0, z=0)

        if self.stage == FlightStage.BASE:

            total_force = self.weight().add(
                vector=self.engine().add(
                    vector=self.drag()
                )
            )

            self.setFlightStage(data=data, total_force=total_force)

            if total_force.z < 0:
                return Vector(x=0, y=0, z=0)
            else:
                return total_force.divide(scalar=ROCKET_MASS)

        elif self.stage == FlightStage.LAUNCH_RAIL:

            total_force = self.weight().add(
                vector=self.engine().add(
                    vector=self.drag()
                )
            )

            self.setFlightStage(data=data, total_force=total_force)

            return total_force.divide(scalar=ROCKET_MASS)

        elif self.stage == FlightStage.PROPELLED:

            total_force = self.weight().add(
                vector=self.engine().add(
                    vector=self.drag()
                )
            )

            self.setFlightStage(data=data, total_force=total_force)

            return total_force.divide(scalar=ROCKET_MASS)

        elif self.stage == FlightStage.BALLISTIC:

            total_force = self.weight().add(
                vector=self.drag()
            )

            self.setFlightStage(data=data, total_force=total_force)

            return total_force.divide(scalar=ROCKET_MASS)

        elif self.stage == FlightStage.PARACHUTE:

            total_force = self.weight().add(
                vector=self.parachute()
            )

            self.setFlightStage(data=data, total_force=total_force)

            return total_force.divide(scalar=ROCKET_MASS)

        return total_force

    @staticmethod
    def drag() -> Vector:
        return Vector(x=0, y=0, z=0)

    @staticmethod
    def launchRail() -> Vector:
        return Vector(x=0, y=0, z=0)

    @staticmethod
    def normalForce() -> Vector:
        return Vector(x=0, y=0, z=0)

    @staticmethod
    def engine() -> Vector:
        return Vector(x=0, y=0, z=0)

    @staticmethod
    def weight() -> Vector:
        return Vector(x=0, y=0, z=0)

    @staticmethod
    def parachute() -> Vector:
        return Vector(x=0, y=0, z=0)

    def setFlightStage(self, data: Data, total_force: Vector) -> None:
        if self.stage == FlightStage.BASE:

            if total_force.z > 0:
                self.stage = FlightStage.LAUNCH_RAIL

        elif self.stage == FlightStage.LAUNCH_RAIL:

            if data.position.z > self.inputs.launch_rail_length:
                self.stage = FlightStage.PROPELLED

        elif self.stage == FlightStage.PROPELLED:

            if self.engine().norm() < 1e-6:
                self.stage = FlightStage.BALLISTIC

        elif self.stage == FlightStage.BALLISTIC:

            if data.velocity.z < 1e-6:
                self.stage = FlightStage.PARACHUTE

