## Challenge: Humidity lock

You can create a humidity lock using the exact same principles as for the temperature lock, but instead of taking the temperature, take a humidity reading.

[[[rpi-sensehat-humidity]]]

See if you can create a humidity lock using these steps:

- Choose a target humidity that is slightly higher than the current humidity. For best results, make the difference quite small as it is hard to achieve a large change in humidity.
- Display a clue that the humidity needs to be increased to reach the target - this could be an image you display on the LED matrix
- Continually check the current humidity against the target humidity
- When the target humidity is reached, display the unlocked graphic


### Testing your lock

If the diff values you chose are sufficiently small, you should be able to simply blow on the humidity sensor which will momentarily raise the humidity.
