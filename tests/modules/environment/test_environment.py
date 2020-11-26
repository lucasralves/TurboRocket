from core.modules.environment.models.air_properties_model import AirPropertiesModel
from core.modules.environment.models.wind_model import WindModel, ConstantWindModel, PowerWindModel, LogarithmicWindModel

import numpy as np
import matplotlib.pyplot as plt


# Air Properties
def testAirProperties() -> None:
    model = AirPropertiesModel()

    altitude_list = np.linspace(0, 20000, num=500)

    temperature = []
    pressure = []
    density = []
    viscosity = []
    sound_speed = []

    for h in altitude_list:
        temperature.append(model.getTemperature(altitude_agl=h))
        pressure.append(model.getPressure(altitude_agl=h))
        density.append(model.getDensity(altitude_agl=h))
        viscosity.append(model.getViscosity(altitude_agl=h))
        sound_speed.append(model.getSoundSpeed(altitude_agl=h))

    plt.figure(1)
    plt.plot(altitude_list, temperature)
    plt.xlabel('Altitude [m]')
    plt.ylabel('Temperature [K]')
    plt.grid()

    plt.figure(2)
    plt.plot(altitude_list, pressure)
    plt.xlabel('Altitude [m]')
    plt.ylabel('Pressure [Pa]')
    plt.grid()

    plt.figure(3)
    plt.plot(altitude_list, density)
    plt.xlabel('Altitude [m]')
    plt.ylabel('Density [kg/m3]')
    plt.grid()

    plt.figure(4)
    plt.plot(altitude_list, viscosity)
    plt.xlabel('Altitude [m]')
    plt.ylabel('Viscosity [Pa.s]')
    plt.grid()

    plt.figure(5)
    plt.plot(altitude_list, sound_speed)
    plt.xlabel('Altitude [m]')
    plt.ylabel('Sound Speed [m/s]')
    plt.grid()

    plt.show()


# Wind Model
def testWind() -> None:
    model = WindModel(
        constant_wind=ConstantWindModel(
            speed_ref=1
        ),
        power_wind=PowerWindModel(
            height_ref=1,
            exponent=0.14,
            speed_ref=1
        ),
        logarithmic_wind=LogarithmicWindModel(
            height_ref=5,
            speed_ref=1,
            surface_roughness=1,
            plane_displacement=2
        )
    )

    altitude_list = np.linspace(0, 20000, num=500)

    constant = []
    power = []
    logarithmic = []

    for h in altitude_list:
        constant.append(model.constant_wind.getWindSpeed())
        power.append(model.power_wind.getWindSpeed(altitude_agl=h))
        logarithmic.append(model.logarithmic_wind.getWindSpeed(altitude_agl=h))

    plt.figure(1)
    plt.plot(constant, altitude_list, label='Constant')
    plt.plot(power, altitude_list, label='Power')
    plt.plot(logarithmic, altitude_list, label='Logarithmic')
    plt.legend()
    plt.xlabel('Altitude [m]')
    plt.ylabel('Velocity [m/s]')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # testAirProperties()
    testWind()
