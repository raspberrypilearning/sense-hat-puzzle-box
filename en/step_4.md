## Set up the structure

+ Open IDLE to start writing your code.

[[[rpi-gui-idle-opening]]]

+ Paste in these comments to define the different sections of your program. Comments will be ignored by Python, but will help you to structure your program.

```python
# Libraries -------------------

# Functions -------------------

# Pixel art -------------------

# Main program ----------------

# Locks -----------------------

# Secret message --------------

```

When you're finished coding this project, the **Locks** section will contain your code to prevent the program from getting to the last line displaying your secret message unless the user has opened all the locks.

+ Add this code in the **Libraries** section to import the `sense_hat` module:

```python
from sense_hat import SenseHat
```

+ Add this code in the **Main program** section to connect to the Sense HAT:

```python
sense = SenseHat()
```

+ In the **Secret message** section, add a message of your choice which the user will only get to see after they have performed all of the correct actions to unlock the puzzle box.

[[[rpi-sensehat-show-message]]]

+ Save and run your program. You will see your secret message appear on the Sense HAT's LED matrix immediately. We need to add some locks!
