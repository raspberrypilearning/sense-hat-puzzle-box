## Temperature lock

Using the Sense HAT's temperature sensors, this lock will require the user to raise or lower the temperature by a number of degrees in order to unlock.

### How will the lock work?

The lock will work as follows:

- Choose a target temperature close to the current temperature
- Display a colour clue as to whether the Sense HAT is too cold or too hot compared to the target temperature
- Continually check the current temperature against the target temperature
- When the target temperature is reached, display the unlocked graphic

The list above roughly describes the program you're going to write and is called an **algorithm** or a set of instructions.

### Choose a target temperature

+ In the **locks** section, create a variable called `current_temp` and assign it the value of a reading from the Sense HAT to find the current temperature.

Take a look at this information to find out how to take a temperature reading, and add the one line of code you need to your program.

[[[rpi-sensehat-temperature]]]

+ Next, create a list of numbers called `temp_diffs`, containing a range of numbers that could be added or subtracted from your current temperature. The wider this range of numbers, the harder the lock is going to be to break.

```python
temp_diffs=[
  -1.5,-1.4,-1.3,-1.2,-1.1,-1,-0.9,-0.8,-0.7,-0.6,
  0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5
]
```

+ Create another new variable called `diff`. Choose a temperature difference at random from the list and assign this as the variable's value.

[[[generic-python-random-choice]]]

+ Create a new variable called `target_temp` which is equal to the `current_temp` plus the randomly chosen difference. Print out the value of this variable so you can see whether your code worked. You can remove the `print` once you have checked your code works.

--- hints ---

--- hint ---
Use the `get_temperature` method to obtain the current temperature. This is called the **ambient temperature**.
--- /hint ---

--- hint ---
Don't forget to add the import statement to your **libraries** section to allow you to use the random choice function:

```python
from random import choice
```
--- /hint ---

--- hint ---
Here is how your code should look:

```python
current_temp = sense.get_temperature()
temp_diffs=[
  -1.5,-1.4,-1.3,-1.2,-1.1,-1,-0.9,-0.8,-0.7,-0.6,
  0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5
]
diff = choice(temp_diffs)
target_temp = current_temp + diff
print(target_temp)
```

--- /hint ---
--- /hints ---

### Display a colour clue

You need to give your user a visual clue as to what they need to do to unlock the temperature lock. For example, you could display blue on the Sense HAT's LED matrix if the current temperature is too cold, or red if it is currently too hot.

+ Find out the code you will need to display a colour on the Sense HAT's LED matrix from the information below:

[[[rpi-sensehat-display-colour]]]

+ Write an `if` statement to check whether the `current_temp` is greater than the `target_temp`. If it is, display red on the LED matrix, and if not display blue.

[[[generic-python-conditional-selection-with-boolean]]]

--- hints ---
--- hint ---
Use the `clear()` method to display a colour on the LED matrix, and put the RGB values of the colour you would like in the brackets. For example, to fill the screen with green you would write

```python
sense.clear(0, 255, 0)
```
--- /hint ---
--- hint ---
You will need to use an `if`/`else` statement to decide whether the current temperature is greater than (`>`) the target temperature. The `else` part should contain the code you want to run if the current temperature is not greater than the target temperature.
--- /hint ---

--- hint ---
Here is how your code should look:

```python
if current_temp > target_temp:
  sense.clear(255,0,0)
else:
  sense.clear(0,0,255)
```
--- /hint ---
--- /hints ---

+ If you run your code, you will only see a brief flash of the colour before your secret message is revealed. Add a `#` before your secret message to comment it out so that you can more easily see which colour is displayed.

![Comment out](images/comment-out.png)

You can remove the `#` once you know your lock is working properly.

### Continually check the temperature

At the moment your lock will only check the temperature once. The next part of your lock program is to repeatedly check the temperature until it reaches, or is close to, the target temperature.

You can use the `abs()` function to find out how big the difference between the current temperature and the target temperature is, ignoring whether the difference is positive or negative.

```python
abs(target_temp - current_temp)
```

+ Create a `while` loop that runs while the difference between the current temperature and the target temperature is larger than 0.1. Put the code you wrote to display the colours in the while loop by **indenting** it.

[[[generic-python-while-counter]]]

--- hints ---
--- hint ---
Use the `abs()` function to find the size of the difference between the temperatures, and then compare that difference to 0.1
--- /hint ---

--- hint ---
Here is how your code should look:

![Using abs](images/using-abs.png)
--- /hint ---

--- /hints ---

1. Begin a `while` loop which will only end when the current temperature is close enough to the target temperature. The `abs()` function is used to find the size of the temperature difference, by ignoring whether it's positive or negative.

  `while abs(diff) > 0.1:`

  This `while` loop will end when the current temperature is within 0.1 degrees of the target temperature.

1. Add code within your loop to find the new current temperature and store it as **temp**, before using it to recalculate the difference(**diff**) from the target temperature. Your should also print out the **diff** so that you can test your program.

  ```Python3
  while abs(diff) > 0.1:
      temp = sense.get_temperature()

      diff = target_temp - temp
      print(diff)
  ```

  When you run your program by pressing F5, you should eventually see some numbers scroll past indicating the current temperature difference. Over time, you should be able to increase or decrease the temperature until it gets close enough and unlocks.

![Idle Output](images/temp_diffs.png)


### Display the unlock picture

## Testing your lock

To test your lock, you could carefully hold your Raspberry Pi above a hot or cold drink to affect the temperature.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zIgaA9zaaA4" frameborder="0" allowfullscreen></iframe>
