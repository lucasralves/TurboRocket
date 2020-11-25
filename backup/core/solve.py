from typing import Dict

# Visualization
from backup import core as folders, core as env_visualization, core as drag_visualization, core as terminal
from backup.core import RocketModel

from backup.core import EnvironmentSettings

def run(rocket: RocketModel, simulation: Dict) -> None:
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
    drag_visualization.drag_mach_reynolds_plot(path=path, rocket=rocket)

    # Finished
    terminal.finished()