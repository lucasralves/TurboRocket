# ROCKET INPUT
# 1) The rocket is composed of 4 parts:
#   - nose
#   - body
#   - transition
#   - fin
# 2) Each part has an index, which correspond to its position starting from the rocket tip.
# 3) The fins are located on the base of a body and both have the same index.
# 4) All the dimensions are in millimeter and the swept angle is in degrees.

###########################################################################################
# Python libraries
from typing import List

# Models
from core.modules.rocket.models.body_model import BodyModel
from core.modules.rocket.models.fin_model import FinModel
from core.modules.rocket.models.nose_model import NoseModel
from core.modules.rocket.models.transition_model import TransitionModel
from core.modules.rocket.models.rocket_model import RocketModel

# Enums
from core.modules.rocket.enums.nose_geometry import NoseGeometry

###########################################################################################
# Modify the methods below and set the correct geometry

def getNose() -> NoseModel:
    nose = NoseModel(
        height=100,
        diameter=40,
        geometry=NoseGeometry.OGIVE,
        index=1,
    )
    return nose

def getBodies() -> List[BodyModel]:
    bodies = [
        BodyModel(
            height=100,
            diameter=40,
            index=2,
        ),
        BodyModel(
            height=300,
            diameter=40,
            index=4,
        ),
    ]
    return bodies

def getTransitions() -> List[TransitionModel]:
    transitions = [
        TransitionModel(
            height=40,
            top_diameter=40,
            bottom_diameter=20,
            index=3,
        ),
    ]
    return transitions

def getFins() -> List[FinModel]:
    fins = [
        FinModel(
            root_chord=40,
            tip_chord=40,
            number_of_fins=4,
            swept_angle=40,
            index=4,
            leading_edge_diameter=30,
            span=50,
            max_thickness=30,
            trailing_edge_diameter=0
        ),
    ]
    return fins

###########################################################################################
# Rocket geometry
def getRocket() -> RocketModel:
    rocket = RocketModel(
        nose=getNose(),
        bodies=getBodies(),
        transitions=getTransitions(),
        fins=getFins(),
    )
    return rocket