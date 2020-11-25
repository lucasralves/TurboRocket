# Python packages
import matplotlib.pyplot as plt
from typing import List

# Models
from core.models.simulation.output_model import OutputModel

def makePlots(output: OutputModel) -> None:

    # Plots counter
    i: int = 1

    positionVsTime(
        number=i,
        x=list(map(lambda elem: elem.x, output.position)),
        y=list(map(lambda elem: elem.y, output.position)),
        z=list(map(lambda elem: elem.z, output.position)),
        t=output.time
    )

    i += 1

    velocityVsTime(
        number=i,
        vx=list(map(lambda elem: elem.x, output.velocity)),
        vy=list(map(lambda elem: elem.y, output.velocity)),
        vz=list(map(lambda elem: elem.z, output.velocity)),
        t=output.time
    )

    plt.show()

def positionVsTime(number: int, x: List[float], y: List[float], z: List[float], t: List[float]):
    plt.figure(number)
    plt.plot(t, x, label='x')
    plt.plot(t, y, label='y')
    plt.plot(t, z, label='z')
    plt.legend()
    plt.grid()
    plt.xlabel('Time [sec]')
    plt.ylabel('Position [m]')

def velocityVsTime(number: int, vx: List[float], vy: List[float], vz: List[float], t: List[float]):
    plt.figure(number)
    plt.plot(t, vx, label='x')
    plt.plot(t, vy, label='y')
    plt.plot(t, vz, label='z')
    plt.legend()
    plt.grid()
    plt.xlabel('Time [sec]')
    plt.ylabel('Velocity [m/s]')