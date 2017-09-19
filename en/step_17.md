## Are we nearly there yet?

Your user is unlikely to receive GPS signals unless they're outside, so you need to check whether they have a signal and if not prompt them to talk a walk. Before you do that there are a couple of other steps to take.

+ Start a loop which will pick each target from the `targets` list

+ Inside the loop, set a variable called `distance` with the initial ridiculous value of 999999 (km) - this is about 25x the distance around the Earth!

This value means that the program assumes the next location is far away, until it can work out an accurate distance.

--- hints ---
--- hint ---
Use a `for` loop to loop through each location in the `targets` list.
--- /hint ---

--- hint ---
Here is how your code should look:

```python
for target in targets:
    distance = 999999
```
--- /hint ---
--- /hints ---

+ Start a `while` loop within the for loop, which will continue until your current position is less than 10m (0.01km) from the target position.


+ Within the loop, check whether your GPS object is communicating with 4 or more satellites; if not, the user is told to go outside.

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

+ Test this out; if you run your program you should be prompted to go outside. At this point you can either go outside or hang your GPS antenna out a window and it should start to get a GPS signal.

Once your program begins receiving GPS data, it won't currently do anything with it. You'll need to first calculate the distance to the current target and check whether the user is getting closer or farther away.

The **piGPS** library you imported earlier has a built-in function to calculate the distance to the current target.

+ Add an `else` to your `if` to contain the code that will be executed if the GPS receiver can see enough satellites.

+ Within the `else` block, create a new variable called `last_distance` and set it equal to the `distance`

+ Find the distance to the target location using `gps.distanceToTarget(target)`

+ Round this value to 2 decimal places

--- hints ---
--- hint ---
You can use the `round` function built in to Python to round your number. This function takes two arguments - the first is the number, and the second is the number of places to round it to. For example, this code would round the given number to 4 decimal places.

```python
round( 0.2245243432432, 4)
```

--- /hint ---
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
    lastDistance = distance
    distance = round(gps.distanceToTarget(target),2)
```
--- /hint ---
--- /hints ---

+ Still within the `else`, add some code to check whether the user has got closer or further away. Display the text "warmer" or "colder" depending on whether they moved closer or further from the target location.

--- hints ---
--- hint ---
Compare the current distance to the `last_distance`. If the current distance is lower, display "warmer", otherwise display "colder"
--- /hint ---
--- hint ---
You also need to check whether *last_distance* = 999999. If it was then it should be ignored, so that the user isn't told they have got closer just because a GPS lock has been achieved.
--- /hint ---
--- hint ---
Here is how your code might look:

```python
if distance < lastDistance and lastDistance !=999999:
    sense.show_message("Warmer...")
elif distance > lastDistance:
    sense.show_message("Colder...")
```
--- /hint ---
--- /hints ---

### Challenge
Can you display the distance from the target as well as warmer or colder?
