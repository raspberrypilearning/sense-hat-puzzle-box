## Arriving at the location

+ Display the `locked` symbol for five seconds after each GPS check.

--- hints ---
--- hint ---
You have already done this before with the other locks, so see if you can look back at your code and find the right part to copy.
--- /hint ---
--- hint ---
Here is how the new code should look. Add this code within the while loop, after your `if/else` statement.
```python
sense.set_pixels(locked)
sleep(5)
```
--- /hint ---
--- /hints ---

Each time the user reaches a target location, your program should notify them.

+ Add some code to display the green tick (or your chosen icon) once the while loop ends, indicating the user has found the correct location.

```python
sense.set_pixels(tick)
sleep(5)
```

+ Once the for loop completes, all the targets have been found, so display the `unlocked` image when that happens.

### Testing your lock

This lock is tricky to test as you need to go outside. Connect your Raspberry Pi to a battery pack and have a wander.
