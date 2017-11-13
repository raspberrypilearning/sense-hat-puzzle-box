## Temperature lock

This lock will require the user to raise or lower the temperature measured by the Sense HAT's temperature sensors by a number of degrees in order to be opened.

### How will the lock work?

You will do the following to set up this lock:

- Choose a target temperature close to the current temperature
- Display a colour clue as to whether the Sense HAT is too cold or too hot compared to the target temperature
- Continually check the current temperature against the target temperature
- When the target temperature is reached, display the `unlocked` graphic

The list above is called an **algorithm**: a set of instructions which roughly describe the program you're going to write.
