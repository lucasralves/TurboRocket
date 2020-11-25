# Python packages
import matplotlib.pyplot as plt
import numpy as np
from typing import List

# Results
from backup.results import TEMPERATURE_FIG
from backup.results import PRESSURE_FIG
from backup.results import DENSITY_FIG
from backup.results import VISCOSITY_FIG
from backup.results import WIND_FIG

# Environment and Wind
from backup.core import EnvironmentSettings
import wind as wind_model

def environment_plots(path: str, environment: EnvironmentSettings, max_altitude: float):
    altitude_list_environment = np.linspace(environment.altitude_ref, environment.altitude_ref + max_altitude, num=200)
    altitude_list_wind = np.linspace(0, max_altitude, num=200)
    if TEMPERATURE_FIG:
        create_temperature_plot(path=path, altitude_list=altitude_list_environment, environment=environment)
    if PRESSURE_FIG:
        create_pressure_plot(path=path, altitude_list=altitude_list_environment, environment=environment)
    if DENSITY_FIG:
        create_density_plot(path=path, altitude_list=altitude_list_environment, environment=environment)
    if VISCOSITY_FIG:
        create_viscosity_plot(path=path, altitude_list=altitude_list_environment, environment=environment)
    if WIND_FIG:
        create_wind_plot(path=path, altitude_list=altitude_list_wind)

def create_temperature_plot(path: str, altitude_list: List[float], environment: EnvironmentSettings):
    temperature = []
    for i in altitude_list:
        temperature.append(environment.getTemperature(altitude=i))
    plt.figure(1)
    plt.plot(altitude_list, temperature)
    plt.grid()
    plt.xlabel('Altitude [m]')
    plt.ylabel('Temperature [k]')
    plt.savefig(path + '/02_ENVIRONMENT/temperature.png', bbox_inches='tight')
    plt.close()

def create_pressure_plot(path: str, altitude_list: List[float], environment: EnvironmentSettings):
    pressure = []
    for i in altitude_list:
        pressure.append(environment.getPressure(altitude=i))
    plt.figure(1)
    plt.plot(altitude_list, pressure)
    plt.grid()
    plt.xlabel('Altitude [m]')
    plt.ylabel('Pressure [Pa]')
    plt.savefig(path + '/02_ENVIRONMENT/pressure.png', bbox_inches='tight')
    plt.close()

def create_density_plot(path: str, altitude_list: List[float], environment: EnvironmentSettings):
    density = []
    for i in altitude_list:
        density.append(environment.getDensity(altitude=i))
    plt.figure(1)
    plt.plot(altitude_list, density)
    plt.grid()
    plt.xlabel('Altitude [m]')
    plt.ylabel('Density [kg/m3]')
    plt.savefig(path + '/02_ENVIRONMENT/density.png', bbox_inches='tight')
    plt.close()

def create_viscosity_plot(path: str, altitude_list: List[float], environment: EnvironmentSettings):
    viscosity = []
    for i in altitude_list:
        viscosity.append(environment.getDensity(altitude=i))
    plt.figure(1)
    plt.plot(altitude_list, viscosity)
    plt.grid()
    plt.xlabel('Altitude [m]')
    plt.ylabel('Viscosity [Pa.s]')
    plt.savefig(path + '/02_ENVIRONMENT/viscosity.png', bbox_inches='tight')
    plt.close()

def create_wind_plot(path: str, altitude_list: List[float]):
    wind_x = []
    wind_y = []
    for i in altitude_list:
        aux = wind_model.wind_settings(time=0.0, altitude=i)
        wind_x.append(aux[0])
        wind_y.append(aux[1])
    plt.figure(1)
    plt.plot(wind_x, altitude_list, label='x axis')
    plt.plot(wind_y, altitude_list, label='y axis')
    plt.legend()
    plt.grid()
    plt.ylabel('Altitude [m]')
    plt.xlabel('Wind [m/s]')
    plt.savefig(path + '/02_ENVIRONMENT/wind.png', bbox_inches='tight')
    plt.close()