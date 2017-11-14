## Are we nearly there yet?

Your user is unlikely to receive GPS signals unless they're outside. Therefore, you need to check whether the Pi is getting a signal, and if not, prompt the user to take a walk. But before you do that, there are a couple of other steps to take.

+ Start a loop which will run through each location in the `targets` list.

+ Inside the loop, set a variable called `distance` to the ridiculous initial value of `999999` (the program will interpret it at kilometres) — that's about 25 times the distance around the Earth!

This value means that the program assumes the next location is very far away until it can work out an accurate distance.

--- hints ---
--- hint ---
Use a for loop to loop through each location in the `targets` list.
--- /hint ---

--- hint ---
Here is how your code should look:

```python
for target in targets:
    distance = 999999
```
--- /hint ---
--- /hints ---

+ Within the for loop, start a while loop which will run until your current position is less than 10 m (0.01 km) from the target position.


+ Within the while loop, check whether your GPS object is communicating with four or more satellites. If not, show a message telling the user to go outside.

```python3
for target in targets:
  distance = 999999

  while distance > 0.01:
      if gps.sat < 4:
          sense.show_message(
            "Are you outside?",
            scroll_speed=0.05,
            text_colour=(150,150,150)
          )

```

+ Test this out. If you run your program, you should be prompted to go outside. At this point you can either go outside with your Pi or place it near a window, and then it should start to get a GPS signal.

Once your program begins receiving GPS data, it currently won't do anything with it yet. You'll need to first calculate the distance to the current target and check whether the user is moving closer to it or further away.

The `piGPS` library you imported earlier has a built-in function to calculate the distance to the current target.

+ Add an `else` section below your `if` statement to contain the code that will be executed if the GPS receiver can see enough satellites.

+ Within the `else` section, create a new variable called `last_distance`, and set it equal to the `distance`.

+ Find the distance to the target location using `gps.distanceToTarget(target)` and set this as the new value of the `distance` variable, rounding the value to two decimal places

[[[generic-python-rounding-numbers]]]

--- hints ---
--- hint ---
Here is how your code should look:
```python
if gps.sat < 4:
  sense.show_message(
    "Are you outside?",
    scroll_speed=0.05,
    text_colour=(150,150,150)
  )
else:
    last_distance = distance
    distance = round(gps.distanceToTarget(target),2)
```
--- /hint ---
--- /hints ---

+ Still within the `else` section, add some code to check whether the user has got closer or further away from the target location. As part of the check, test whether `last_distance = 999999`. If it is, do nothing, so that the user isn't told they have got closer just because the Pi has started receiving a GPS signal.

+ Display the text `warmer` or `colder` depending on whether they moved closer or further away.

--- hints ---
--- hint ---
Compare the current value of `distance` to that of `last_distance`. If `distance` is smaller, display `warmer`, otherwise display `colder`.
--- /hint ---
--- hint ---
Here is how your code might look:

```python
if distance < last_distance and last_distance !=999999:
    sense.show_message("Warmer...")
elif distance > last_distance:
    sense.show_message("Colder...")
```
--- /hint ---
--- /hints ---

### Challenge
In addition to the message `warmer` or `colder`, can you display the distance from the target in metres?
