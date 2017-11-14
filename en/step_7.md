## Choose a target temperature

First, you need to record the current temperature.

+ In the **Locks** section, create a variable called `current_temp` and assign it the value of a temperature reading from the Sense HAT.

Take a look at the information section below to find out how to take a temperature reading, and add the one line of code you need to your program.

[[[rpi-sensehat-temperature]]]

+ Next, create a list of numbers called `temp_diffs`, containing a range of numbers that could be added or subtracted from your current temperature. The wider this range of numbers, the harder the lock is going to be to break.

```python
temp_diffs=[
  -1.5,-1.4,-1.3,-1.2,-1.1,-1,-0.9,-0.8,-0.7,-0.6,
  0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5
]
```

+ Create another new variable called `diff`. Choose an item from the `temp_diffs` lists at random and assign it as the `diff` variable's value.

[[[generic-python-random-choice]]]

+ Create a new variable called `target_temp`, and set it equal to the `current_temp` plus the randomly chosen number you stored as `diff`. Print out the value of this variable so you can see whether your code worked. You can remove the `print` statement once you have checked your code.

--- hints ---

--- hint ---
Use the `get_temperature` method to obtain the current temperature. This is called the **ambient temperature**.
--- /hint ---

--- hint ---
Don't forget to add an `import` statement to your **Libraries** section to allow you to use the `random` function:

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
