## Arriving at the location

+ Display the locked symbol for 5 seconds after each GPS Check

--- hints ---
--- hint ---
You have already done this before with the other locks, so see if you can look back at your code and find the right part to copy.
--- /hint ---
--- hint ---
Here is how the new code should look:
```python
pixels(locked)
sleep(5)
```
--- /hint ---
--- /hints ---

Each time the user reaches a target location, your program should notify them.

+ Add some code to display the green tick (or your chosen icon) once the `while` loop ends, indicating the user has found the correct location.

```python
sense.set_pixels(tick)
sleep(5)
```

+ Once the `for` loop completes, all the targets have been found so display the unlocked image.

## Testing your lock

This lock is tricky to test as you need to go outside. Connect your Raspberry Pi to a battery pack and take a wander.
