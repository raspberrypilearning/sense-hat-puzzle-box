## Puzzle Box - Combination Lock

Using the Sense HAT's orientation sensors, this combination lock will require the user to move the Sense HAT in certain directions in order to unlock it.

### How will the lock work?

The lock will work as follows:

  - Set up a sequence of angles that will be the combination
  - Repeatedly check the orientation of the Sense HAT and convert it to an angle
  - Compare this angle with each item in the combination in order
  - If the angle matches, continue to the next item; if not, go back to the beginning of the sequence
  - Once all items in the combination are complete, display the unlocked graphic

The list above roughly describes the program you're going to write and is called an **algorithm** or a set of instructions.
