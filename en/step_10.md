## Challenge: Pressure lock

You can create a pressure lock using the exact same principles as for the temperature lock, but instead of taking the temperature, take a pressure reading.

[[[rpi-sensehat-pressure]]]

See if you can create a pressure lock using these steps:

- Choose a target pressure that is slightly higher than the current pressure. For best results, make the difference quite small as it is hard to achieve a large change in pressure.
- Display a clue that the pressure needs to be increased to reach the target - this could be an image you display on the LED matrix
- Continually check the current pressure against the target pressure
- When the target pressure is reached, display the unlocked graphic


### Testing your lock

If the diff values you chose are sufficiently small, you should be able to simply blow on the pressure sensor which will momentarily raise the pressure.
