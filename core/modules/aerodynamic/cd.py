# 1) This file calculates the drag coefficient as a function of Mach Number, Reynolds Number and
# geometric parameters of the rocket.

#################################################################################################
# Python packages
import math

# Rocket Model
from core.modules.rocket.models.rocket_model import RocketModel
#################################################################################################
# Constants

SURFACE_COEFF_SKIN_FRICTION = 0.15  # 0.15 - no heat transfer; 0.0512: cooled wall
REYNOLDS_LAMINAR_LIMIT = 5 * 1e5


#################################################################################################

class DragCoefficientBarrowman:
    rocket: RocketModel

    def __init__(self, rocket: RocketModel):
        self.rocket = rocket
        self.critic_reynolds = 51 * ((rocket.mean_surface_roughness / rocket.total_height) ** -1.039)

    ##############################################################################################
    # FRICTION DRAG

    # Skin friction coefficient
    def skin_friction_coefficient(self, reynolds: float, mach: float) -> float:

        Cf: float  # Skin friction coefficient
        Cfc: float  # Compressible skin friction coefficient

        # Skin friction coefficient calculation
        if reynolds <= REYNOLDS_LAMINAR_LIMIT:
            Cf = 1.328 / math.sqrt(reynolds)
        else:
            if reynolds < self.critic_reynolds:
                Cf = (1 / ((3.46 * math.log10(reynolds) - 5.6) ** 2)) - 1700 / reynolds
            else:
                Cf = 0.032 * ((self.rocket.mean_surface_roughness / self.rocket.total_height) ** 0.2)

        # Compressibility correction
        if mach < 1:
            if REYNOLDS_LAMINAR_LIMIT < reynolds < self.critic_reynolds:
                Cfc = Cf * (1 - 0.09 * (mach ** 2))
            else:
                Cfc = Cf * (1 - 0.12 * (mach ** 2))
        else:
            if reynolds <= REYNOLDS_LAMINAR_LIMIT:
                Cfc = Cf / ((1 + 0.045 * (mach ** 2)) ** 0.25)
            elif REYNOLDS_LAMINAR_LIMIT < reynolds < self.critic_reynolds:
                Cfc = Cf / (1 + SURFACE_COEFF_SKIN_FRICTION * (mach ** 0.58))
            else:
                if (1 + SURFACE_COEFF_SKIN_FRICTION * (mach ** 0.58)) > (1 - 0.18 * (mach ** 2)):
                    Cfc = Cf / (1 - 0.18 * (mach ** 2))
                else:
                    Cfc = Cf / (1 + SURFACE_COEFF_SKIN_FRICTION * (mach ** 0.58))

        return Cfc

    # Friction drag coefficient
    def friction_drag_coefficient(self, reynolds: float, mach: float) -> float:

        Cdf: float

        # Skin friction coefficient
        Cfc = self.skin_friction_coefficient(reynolds=reynolds, mach=mach)

        # Friction drag coefficient
        Cdf = Cfc * self.rocket.surface_area / self.rocket.reference_area

        return Cdf

    ##############################################################################################
    # PRESSURE DRAG

    # Tail
    def tail_pressure_drag(self, reynolds: float, mach: float) -> float:

        # Leading edge drag
        leading_delta_cd: float = 0.0

        # Thickness drag
        thickness_sonic_correction: float

        # Trailing drag
        trailing_sonic_correction: float
        Cfb: float

        # Output
        Cd_tail: float = 0.0

        # ---------------------------
        # Leading edge drag
        if mach < 0.9:
            leading_delta_cd = (1 - (mach ** 2)) ** -0.417 - 1
        elif 0.9 < mach < 1:
            leading_delta_cd = 1 + 1.5 * (mach - 0.9)

        for element in self.rocket.fins:
            Cd_tail += 2 * element.number_of_fins * (math.cos(element.swept_angle * math.pi / 180) ** 2) * leading_delta_cd * (element.span * element.leading_edge_diameter / (2 * self.rocket.reference_area))

        # ---------------------------
        # Trailing edge drag
        for element in self.rocket.fins:
            if element.trailing_edge_diameter != 0:
                if mach < 1:
                    trailing_sonic_correction = (math.cos(element.swept_angle) ** 2) * ((0.223 - 4.02 * self.skin_friction_coefficient(reynolds=reynolds / mach, mach=1) * (element.trailing_edge_diameter / element.max_thickness)) ** 2) / (self.skin_friction_coefficient(reynolds=reynolds, mach=mach) * self.skin_friction_coefficient(reynolds=reynolds / mach, mach=mach) / element.max_thickness)
                    Cfb = self.skin_friction_coefficient(reynolds=reynolds, mach=mach) * element.trailing_edge_diameter * math.sqrt((element.span * math.sin(element.swept_angle * math.pi / 180) - element.root_chord + element.tip_chord) ** 2 + element.span ** 2)
                    Cd_tail += 0.135 * element.number_of_fins * (element.trailing_edge_area / element.one_fin_lateral_area) / ((Cfb ** (1 / 3)) * math.sqrt(trailing_sonic_correction - mach * mach * ((element.span / (element.span * math.sin(element.swept_angle * math.pi / 180) + element.tip_chord - element.root_chord)) ** 2)))

        # ---------------------------
        # Thickness drag
        for element in self.rocket.fins:
            if mach < 1:
                thickness_sonic_correction = (math.cos(element.swept_angle) * math.pi / 180) + (((element.thickness_pressure_drag_cdtt / self.skin_friction_coefficient(reynolds=reynolds / mach, mach=1)) * (self.rocket.reference_area / element.one_fin_lateral_area) - 4 * (element.max_thickness / element.root_chord) * math.cos(element.swept_angle * math.pi / 180)) / (120 * ((element.max_thickness / element.root_chord) ** 4) * (math.cos(element.swept_angle) ** 2))) ** (2 / 3)
                Cd_tail += element.number_of_fins * self.skin_friction_coefficient(reynolds=reynolds, mach=mach) * (element.one_fin_lateral_area / self.rocket.reference_area) * (4 * (element.max_thickness / element.root_chord) * math.cos(element.swept_angle * math.pi / 180) + (120 * ((element.max_thickness / element.root_chord) ** 4) * (math.cos(element.swept_angle) ** 2)) / ((thickness_sonic_correction - mach * mach * (math.cos(element.swept_angle * math.pi / 180) ** 2)) ** (3 / 2)))

        return Cd_tail

    # --------------------------------
    # Forebody
    def forebody_pressure_drag(self, reynolds: float, mach: float) -> float:

        sonic_correction: float
        Cdp_sonic: float
        cdp: float

        if self.rocket.nose.geometry == 'ogive':
            Cdp_sonic = 0.88 / ((self.rocket.nose.height / self.rocket.nose.diameter + 1) ** 2.22)
        else:
            Cdp_sonic = 0.88 / ((self.rocket.nose.height / self.rocket.nose.diameter + 0.7) ** 1.29)

        sonic_correction = 1 + (6 * self.rocket.surface_area * self.skin_friction_coefficient(reynolds=reynolds / mach, mach=1) / (self.rocket.reference_area * Cdp_sonic * ((self.rocket.total_height / self.rocket.nose.diameter) ** 3))) ** (5 / 3)
        Cdp = 1e-3 * 6 * self.rocket.surface_area * self.skin_friction_coefficient(reynolds=reynolds, mach=mach) / ((self.rocket.total_height / math.sqrt(self.rocket.reference_area * 4 / math.pi) ** 3) * self.rocket.reference_area * ((sonic_correction - mach * mach) ** 0.6))

        return Cdp

    #--------------------------------
    # Base
    def base_pressure_drag(self, reynolds: float, mach: float) -> float:

        hr: float = 1
        cr: float = 1

        for element in self.rocket.fins:
            hr = element.trailing_edge_diameter
            cr = element.root_chord

        k = 1 + 1 / ((6.38 + 39.7 * (hr / cr)) * self.skin_friction_coefficient(reynolds=reynolds / mach, mach=1) * (self.rocket.surface_area / (0.25 * math.pi * self.rocket.base_diameter ** 4)))

        Cdb_sonic = ((0.25 * math.pi * self.rocket.base_diameter ** 4) / self.rocket.reference_area) * (0.185 + 1.15 * (hr / cr))

        Mach_cr = 0.892 / math.sqrt(Cdb_sonic)

        if mach < 1:
            Cdb = (0.29 * ((0.25 * math.pi * self.rocket.base_diameter ** 4) / self.rocket.reference_area)) / math.sqrt(self.skin_friction_coefficient(reynolds=reynolds, mach=mach) * (self.rocket.surface_area / (0.25 * math.pi * self.rocket.base_diameter ** 4)) * (k - mach ** 2))
        elif 1 < mach < Mach_cr:
            Cdb = Cdb_sonic * (0.88 + 0.12 * math.exp(-3.38 * (mach - 1)))
        else:
            Cdb = 0.7 * ((0.25 * math.pi * self.rocket.base_diameter ** 4) / self.rocket.reference_area) / (mach ** 2)

        return Cdb

    # Total pressure drag
    def pressure_drag_coefficient(self, reynolds: float, mach: float) -> float:
        return self.tail_pressure_drag(reynolds=reynolds, mach=mach) + self.forebody_pressure_drag(reynolds=reynolds, mach=mach) + self.base_pressure_drag(reynolds=reynolds, mach=mach)

    def drag_coefficient(self, reynolds: float, mach: float) -> float:
        return self.pressure_drag_coefficient(reynolds=reynolds, mach=mach) + self.friction_drag_coefficient(reynolds=reynolds, mach=mach)