# FILE INFORMATION
#---------------------------------------------------------------------------#
# This file calculates the aerodynamic coeficients, forces an moments

# Coeficients calculation:
# ./src/cd.py - drag coefficient
# ./src/cn.py - normal force coefficient
# ./src/cm.py - lateral moment coefficient
# ./src/cl_dampping.py - roll dampping moment
# ./src/cm_dampping.py - lateral dampping moment

# Center of pressure calculation:
# ./src/cp.py - center of pressure
#---------------------------------------------------------------------------#

# PACKAGES
#---------------------------------------------------------------------------#
# Helpers
from dataclasses import dataclass

# Model
from models.geometry.rocket_model import RocketModel

#---------------------------------------------------------------------------#

@dataclass
class Aerodynamic:

    # Inputs
    rocket: RocketModel

    # Calculated
    # force_constant: float
    # moment_constant: float
    # cm: float
    # cn: float
    # cl_dampping: float
    # cm_dampping: float

    @classmethod
    def setCalculatedParameters() -> None:
        self.force_constant = 0.0
        self.moment_constant = 0.0
        self.cm_derivative = 0.0
        self.cn_derivative = 0.0
        self.cl_dampping_derivative = 0.0
        self.cm_dampping_derivative = 0.0

    # Coefficients
    #------------------------------------------------------------------
    @classmethod
    def getCd(self, alpha: float) -> float:
        return 0.0

    @classmethod
    def getCn(self, alpha: float) -> float:
        return self.cn_derivative * alpha

    @classmethod
    def getCm(self, alpha: float) -> float:
        return self.cm_derivative * alpha

     @classmethod
    def getCmDampping(self, lateral_angular_velocity: float) -> float:
        return self.cm_dampping_derivative * lateral_angular_velocity

    @classmethod
    def getClDampping(self, roll_angular_velocity: float) -> float:
        return self.cl_dampping_derivative * roll_angular_velocity

    # Forces and Moments
    #------------------------------------------------------------------
    @classmethod
    def getDrag(self) -> float:
        return self.getCd() * self.force_constant

    @classmethod
    def getNormalForce(self, alpha: float) -> float:
        return self.getCn(alpha=alpha) * self.force_constant

    @classmethod
    def getLateralMoment(self, alpha: float) -> float:
        return self.getCm(alpha=alpha) * self.moment_constant

    @classmethod
    def getLateralDamppingMoment(self, lateral_angular_velocity: float) -> float:
        return self.getCmDampping(lateral_angular_velocity=lateral_angular_velocity) * self.moment_constant

    @classmethod
    def getRollDamppingMoment(self, roll_angular_velocity: float) -> float:
        return self.getClDampping(roll_angular_velocity=roll_angular_velocity) * self.moment_constant
