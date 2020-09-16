
# Visualization
import core.visualization.make_results_folder as folders
import core.visualization.environment_visualization as env_visualization
import core.visualization.terminal_output as terminal

from core.simulation.wind_settings import WindSettings
from core.simulation.environment_settings import EnvironmentSettings

def run():
    # Create directories
    path = folders.create_simulation_case()
    terminal.create_folder(path)

    # Simulate
    terminal.simulation_started()
    terminal.simulation_status()

    terminal.simulation_finished()

    # Create simulation outputs
    terminal.save_results()

    # Create environment outputs
    env_visualization.environment_plots(path=path, environment=EnvironmentSettings(), max_altitude=3000)

    # Finished
    terminal.finished()