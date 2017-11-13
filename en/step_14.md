## Check the combination

To check the combination, you'll need to create a loop which will continue until the `combination` list has been emptied. For this you'll use a `while` loop.

To find the number of items in a list, you can use the `len()` function to determine the length of the list, like this:

```python
len(combination)
```

+ In the **Locks** section, create a `while` loop which will run while the number of items in the `combination` list is greater than 0.

+ Inside the loop, get the acceleration data from the sensor using `get_accelerometer_raw`. Then, create two variables called `x` and `y` to store the x and y data respectively.

```python
while len(combination) > 0:
  acc = sense.get_accelerometer_raw()
  x = acc["x"]
  y = acc["y"]
```

+ Create a new variable called `angle`, then convert `x` and `y` to an angle using the `get_angle` function you wrote earlier, and store the result in this `angle` variable.

+ Write an `if` statement to compare the value of `angle` with the first item in the `code` list and check whether they are the same.

[[[generic-python-list-index]]]

+ If they are the same (i.e. the player has rotated the Sense HAT to the correct angle), `pop` the first item from the combination list and `append` it to the complete list, like this.

```python
if angle == combination[0]:
   complete.append(combination.pop(0))
```

+ We need to let the player know when they got an angle right. To to this, use the `set_pixel` method to also set a single LED to green for one second if the angle and the first item in the `combination` list are equal. You already have a variable in which you have stored the RGB values for the colour green.

[[[rpi-sensehat-single-pixel]]]

If the user gets the angle wrong, then the `complete` and `combination` lists need to be reset and a red LED should be shown.

+ Add an `else` condition to your `if` block to do the following:

1. Set the `combination` list to be equal to whatever is in the `complete` list plus whatever is left in the `combination` list
1. Clear the `complete` list
1. Display a red pixel for one second to show the user they made a mistake

--- hints ---
--- hint ---
You can add lists together just like you would with numbers, so the `+` operator will add the contents of one list to another.
--- /hint ---

--- hint ---
To clear a list, simply set it equal to a blank list `[]`.
--- /hint ---

--- hint ---
You already defined the colour red as `r` when you set up the padlock images earlier, so you can reuse that variable when you display the red pixel.
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

Finally, you'll need to add some code to give the user time to rotate their Sense HAT and then say when they are ready to try the next angle. To do this, we will check the next angle only when the joystick is pressed.

+ As the first action inside your loop, add a line of code to wait for the joystick to be pressed. Put the rest of the code from your loop inside a condition so that it only happens if the joystick was pressed.

```python
event = sense.stick.wait_for_event()
if event.action == "pressed":
```

+ Once the loop stops, the combination has been found, so display the `locked` picture and wait for two seconds, then display the `unlocked` picture and wait for another two seconds to show that the combination lock has been opened.

### Testing your lock
To test the lock, run your program and rotate the Sense HAT. You may want to temporarily comment out the code for your other locks (using `#`) so that you only have one lock to test.
