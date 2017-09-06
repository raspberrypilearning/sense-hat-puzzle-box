## Check the combination

To check the combination, you need to create a loop which will continue until the `code` list has been emptied. For this you'll need a `while` loop.

+ Create a `while` loop which will run while the number of items in the `combination` list is greater than 0.

To find the number of items in a list, you can use the `len()` function to find the length of the list, like this:

```python
len(combination)
```

+ Inside the loop, get the acceleration data from the sensor using `get_accelerometer_raw`. Then, create two variables called `x` and `y` to store the x and y data respectively.s

```python
while len(combination) > 0:
  acc = sense.get_accelerometer_raw()
  x = acc["x"]
  y = acc["y"]
```

+ Create a new variable called `angle`, then convert `x` and `y` to an angle using the `get_angle` function you wrote earlier and store the result in this variable.

+ Write an `if` statement to compare the angle with the first item in the `code` list.

[[[generic-python-list-index]]]

```python
if get_angle(x,y) == code[0]:
   complete.append(code.pop(0))
   sense.set_pixel(0,0,g)
```

- The condition `get_angle(x,y) == code[0]` uses the `get_angle` function to convert `x` and `y` to an angle. It then checks whether the angle matches the first item in `code`.
- If the angle matches then the line `complete.append(code.pop(0))` removes (or "pops") the first item from `code` and adds it to the `complete` list.
- The `sense.set_pixel(0,0,g)` line turns a single LED green to inform the user they got that step right.

1. If the user gets the angle wrong then the `complete` and `code` lists reset and a red LED is shown. Add the following `else` condition to your `if` block:

```python
if get_angle(x,y) == code[0]:
   complete.append(code.pop(0))
   sense.set_pixel(0,0,g)
else:
   code = complete + code
   complete = []
   sense.set_pixel(0,0,r)
```

1. Finally, you'll need to add some `sleep` commands to give the user time to rotate their Sense HAT. Using two sleep commands and turning the LED off in between will create a flashing LED that informs the user whether they've got the steps correct.

```python
sleep(1)
sense.set_pixel(0,0,e)
sleep(1)
```


## Testing your lock
