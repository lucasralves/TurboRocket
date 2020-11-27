from core.modules.aerodynamic.cd import DragCoefficientBarrowman
from tests.modules.aerodynamic.rocket import getRocket
from core.modules.rocket.models.rocket_model import RocketModel

import numpy as np

import matplotlib.pyplot as plt

def testAerodynamic():
    rocket: RocketModel = getRocket()
    rocket.setCalculatedParameters(cg=300)
    drag = DragCoefficientBarrowman(rocket=rocket)

    reynolds = 1e6
    mach = np.linspace(0, 0.7, num=10)

    viscous_drag = []
    forebody_drag = []

    pressure_drag = []

    for i in mach:
        viscous_drag.append(drag.friction_drag_coefficient(reynolds=reynolds, mach=i))
        forebody_drag.append(drag.forebody_pressure_drag(reynolds=reynolds, mach=i))
        # pressure_drag.append(drag.pressure_drag_coefficient(reynolds=reynolds, mach=i))

    plt.figure(1)
    plt.plot(mach, viscous_drag, label='Viscous drag')
    plt.grid()
    plt.xlabel('Mach')
    plt.ylabel('Coefficient')
    plt.legend()

    plt.show()


if __name__ == '__main__':
    testAerodynamic()
