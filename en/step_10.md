## Challenge: humidity lock

You can create a humidity lock using the exact same principles as for the temperature lock, but instead of taking the temperature, take a humidity reading.

[[[rpi-sensehat-humidity]]]

See if you can create a humidity lock using the steps in this algorithm:

- Choose a target humidity that is slightly higher than the current humidity. For best results, make the difference quite small as it is hard to achieve a large change in humidity.
- Display a clue on the LED matrix so that the user knows the humidity needs to be increased to reach the target — the clue could be an image.
- Continually check the current humidity against the target humidity.
- When the target humidity is reached, display the `unlocked` graphic.

### Testing your lock

If the difference between the current and the target humidity you chose is sufficiently small, you should be able to simply blow on the humidity sensor to momentarily raise the humidity.
