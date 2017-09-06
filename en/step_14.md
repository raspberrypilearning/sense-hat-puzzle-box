## Check the combination

To check the combination, you need to create a loop which will continue until the `combination` list has been emptied. For this you'll need a `while` loop.

To find the number of items in a list, you can use the `len()` function to find the length of the list, like this:

```python
len(combination)
```

+ Still in the **locks** section, create a `while` loop which will run while the number of items in the `combination` list is greater than 0.

+ Inside the loop, get the acceleration data from the sensor using `get_accelerometer_raw`. Then, create two variables called `x` and `y` to store the x and y data respectively.

```python
while len(combination) > 0:
  acc = sense.get_accelerometer_raw()
  x = acc["x"]
  y = acc["y"]
```

+ Round the `x` and `y` values to zero decimal places using the `round` function

+ Create a new variable called `angle`, then convert `x` and `y` to an angle using the `get_angle` function you wrote earlier and store the result in this variable.

+ Write an `if` statement to compare the angle with the first item in the `code` list and check whether they are the same.

[[[generic-python-list-index]]]

+ If they are the same (i.e. the player has turned the Sense HAT to the correct angle), `pop` the first item from the combination list and `append` it to the complete list, like this.

```python
if get_angle(x,y) == combination[0]:
   complete.append(combination.pop(0))
```

+ We need to let the player know when they got an angle right, so use the `set_pixel` method to also set a single LED to green if the angle and the first item in the combination were equal.

[[[rpi-sensehat-single-pixel]]]

If the user gets the angle wrong then the `complete` and `combination` lists need to be reset and a red LED should be shown.

+ Add an `else` condition to your `if` block which does the following:

1. Set the combination list to be equal to whatever is in the `complete` list plus whatever is left in the `combination` list
1. Clear the `complete` list
1. Display a red pixel to show the user they made a mistake

--- hints ---
--- hint ---
You can add lists together just like you would with numbers, so the `+` operator will add the contents of one list to another.
--- /hint ---

--- hint ---
To clear a list, simply set it equal to a blank list `[]`.
--- /hint ---

--- hint ---
You already have the colour red defined as `r` from the lock images you created earlier, so you can reuse that when you display the red pixel.
--- /hint ---

--- hint ---
Here is how your code should look:

```python
else:
   combination = complete + combination
   complete = []
   sense.set_pixel(0,0,r)
```
--- /hint ---
--- /hints ---

Finally, you'll need to add some `sleep` commands to give the user time to rotate their Sense HAT.

+ Still inside your loop, wait for 1 second, then turn the LED off (black), then wait for another second.

+ Once the loop stops, the combination has been found, so display the lock picture, then wait for 2 seconds, then display the unlock picture and wait another 2 seconds to show that the combination lock has been broken.

## Testing your lock
To test the lock, run your program and rotate the Sense HAT. You may want to temporarily comment out the code for your other locks so that you only have one lock to test.

This lock is quite difficult to test on the Sense HAT emulator by manipulating the model, so you might need to alter the code to give you more time to rotate the Sense HAT in between each angle. 
