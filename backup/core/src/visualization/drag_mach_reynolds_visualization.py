# Python packages
import numpy as np

# Drag model
from backup.core import DragCoefficientBarrowman

# Rocket model
from backup.core import RocketModel


def drag_mach_reynolds_plot(path: str, rocket: RocketModel) -> None:
    MACH_LIST = np.linspace(1e-3, 0.9, num=10)
    REYNOLDS_LIST = np.linspace(1e4, 1e9, num=5)

    drag_list = []
    drag_coefficient = []

    drag_model = DragCoefficientBarrowman(rocket=rocket)

    for reynolds in REYNOLDS_LIST:
        for mach in MACH_LIST:
            drag_list.append(drag_model.drag_coefficient(reynolds=reynolds, mach=mach))
        drag_coefficient.append(drag_list)
        drag_list = []

    print(drag_coefficient)