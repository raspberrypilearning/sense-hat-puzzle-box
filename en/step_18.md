## Arriving at the location

+ The last bit of feedback to do is to display the locked symbol for 5 seconds, using the two lines shown below:

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
            else:
                lastDistance = distance
                distance = round(gps.distanceToTarget(target),2)

                if distance < lastDistance and lastDistance !=999999:
                    msg = "Warmer...{0}m".format(int(distance*1000))
                    colour = (150,0,0)
                elif distance > lastDistance:
                    msg = "Colder...{0}m".format(int(distance*1000))
                    colour = (0,0,150)

                    sense.show_message(
                      msg,
                      scroll_speed=0.05,
                      text_colour=colour
                    )

            sense.set_pixels(locked)
            sleep(5)
        ```

## Reaching your destination

Each time the user reaches a step in their journey your program should notify them. This is where your pixel art comes in. Add two lines outside your loop to first show the pixel art and then pause before continuing:

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
          else:
              lastDistance = distance
              distance = round(gps.distanceToTarget(target),2)

              if distance < lastDistance and lastDistance !=999999:
                  msg = "Warmer...{0}m".format(int(distance*1000))
                  colour = (150,0,0)
              elif distance > lastDistance:
                  msg = "Colder...{0}m".format(int(distance*1000))
                  colour = (0,0,150)

                  sense.show_message(
                    msg,
                    scroll_speed=0.05,
                    text_colour=colour
                  )

          sense.set_pixels(locked)
          sleep(5)
      sense.set_pixels(tick)
      sleep(5)

      ```

Once this loop completes all the targets, the program will continue either to the next lock or to the hidden message.



## Testing your lock

This lock is tricky to test as you need to go outside. Connect your Raspberry Pi to a battery pack and take a wander.
