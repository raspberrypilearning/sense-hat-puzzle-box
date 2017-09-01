## Adding locks

Now your basic code is ready, it's time to add some locks to protect your secret message. These locks can be added in any order and it's up to you to choose which you will add.

Here are some ideas:

### [Temperature Lock](temp_lock.md)

Using the Sense HAT's temperature sensors, this lock will require the user to raise or lower the temperature by a number of degrees in order to unlock.

### [Orientation Combination Lock](comb_lock.md)

It's possible for the Sense HAT to know which way up it is, and point up, down, left, and right. To break this lock, the user must rotate the device to match a sequence of orientations; for example, the combination might be up, left, up, down and the user would have to rotate the Sense HAT in those directions.

### [Pressure Lock](pressure_lock.md)

The Sense HAT can detect the air pressure around it. This could be changed in a number of ways:

 - Placing the Raspberry Pi in a sealed container and squashing it.
 - Cooling or heating the air in the container before sealing it. The air will expand or contract over time, which will change the pressure.
 - Fast-moving air affects the pressure, and you can detect air being blown onto the Sense HAT.

### [Location Lock](gps_lock.md)

Using some additional hardware, your puzzle box is able to calculate where in the world it is. A really challenging lock would be one that requires the user to go to a specific place.

