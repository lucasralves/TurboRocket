import sys

def create_folder(case: str):
    print('')
    print('1 - CASE FOLDER \'{}\' CREATED'.format(case, ))

def simulation_started():
    print('2 - SIMULATION STARTED')
    print('')
    print('-------------------------------------------------------------------------------------')
    print('{:^85}'.format('SIMULATION STATUS'))
    print('-------------------------------------------------------------------------------------')


def simulation_status(altitude: float = 0.0,
                      velocity: float = 0.0,
                      acceleration: float = 0.0,
                      stage: str = 'Base'):
    print('| Alt.: {:6.2f} [m] | Vel.: {:6.2f} [m/s] | Accel.: {:6.2f} [m/s2] | Stage: {:10s} |'.format(altitude, velocity, acceleration, stage))

def simulation_finished():
    print('')
    print('3 - SIMULATION FINISHED')

def save_results():
    print('4 - SAVING RESULTS')

def finished():
    print('5 - ALL FINISHED')