# Python packages
from dataclasses import dataclass

# Models
from core.models.simulation.input_model import InputModel
from core.models.simulation.output_model import OutputModel

@dataclass
class SimulationModel:
    input: InputModel
    output: OutputModel

