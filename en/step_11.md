## Combination lock

Using the Sense HAT's orientation sensors, the combination lock will require the user to rotate the Sense HAT in certain directions in order to unlock it.

### How will the lock work?

The list below is another algorithm (set of instructions) that roughly describes the program you're going to write.

  - Create a list of angles that will be the combination
  - Repeatedly check the orientation of the Sense HAT and convert it to an angle
  - Compare this angle with each item in the combination list in order
  - If the angle matches, continue to the next item, if not, go back to the beginning of the combination
  - Once all items in the combination list have been found, display the `unlocked` graphic
