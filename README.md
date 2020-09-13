# TurboRocket

This is a python implementation of the trajectory determination program.

### Folder structure:

<pre>
- main
  | - rocket.py
  | - wind.py
  | - problem.py
  | - controll.py
  | - main.py
  |
  | core
  |  | models
  |  |   | rocket
  |  |   |   | - rocket_model.py
  |  |   |   | - nose_model.py
  |  |   |   | - body_model.py
  |  |   |   | - transition_model.py
  |  |   |   | - fin_model.py
  |  |   |  
  |  | simulation 
  |  |   | - environment_settings.py
  |  |   | - wind_settings.py
  |  |  
  |  | math
  |  |   | - differential_equation_solver.py
  |  |   | - quaternion.py
  |  |
  |  | aerodynammic
  |  |   | - barrowman_cn.py
  |  |   | - barrowman_cm.py
  |  |   | - barrowman_cmd.py
  </pre>
