# Trinity Firefighting Competition

Structure of the Code:
A high level bash script runs python scripts in three stages

Stage 1. freq_stimuli.py: keeps running until the required frequency is detected.


Stage 2. blinkBlueLED.py, traverseMaze.py: Blinks a blue LED for activation signal. Traversal keeps going until flame is detected then it stops.


Stage 3: blinkRedLED.py, extinguishCandle.py: Blinks a red LED for fire signal. Extinguishing keeps going until there is no flame around the robot.

