from core.models.simulation.data import Data

def printHeader() -> None:
    print('{:>10} {:>10} {:>10}'.format('Time', 'Altitude', 'Velocity'))

def printData(data: Data) -> None:
    print('{:10.2f} {:10.2f} {:10.2f}'.format(data.time, data.position.z, data.velocity.z))