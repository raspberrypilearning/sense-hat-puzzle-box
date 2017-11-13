## Set the target

If you have followed the instructions, the `piGPS` library should be installed on your Pi.

+ In the **Libraries** section, add this code to import the necessary functionality:

```python3
from pigps import GPS
```

+ Add a pixel art image to your program to indicate when a target location has been reached. We chose a green tick, but you can draw whatever you like.

  ![Green Tick](images/green_tick.png)

To add the tick to your code, create a new list containing the items for the pixel art image in the **Pixel art** section:

```python3
tick = [
e,e,e,e,e,e,e,g,
e,e,e,e,e,e,g,g,
e,e,e,e,e,g,g,e,
e,e,e,e,g,g,e,e,
g,g,e,g,g,e,e,e,
e,g,g,g,e,e,e,e,
e,e,g,e,e,e,e,e,
e,e,e,e,e,e,e,e
    ]
```

The program you're going to write needs at least one location target, but it can have many.

+ In the **Locks** section, create a GPS object called `gps` which will monitor the GPS device and store its raw data as useful data such as longitude, latitude, and altitude.

```python3
gps = GPS()
```

Choose your destination and find out its latitude and longitude using an online mapping service such as [Google Maps](http://maps.google.com).

+ Find your chosen location on the map and right-click on it.

![Map](images/map.png)

+ Select **What's here**, and the latitude and longitude will be shown at the bottom of the screen.

![Map with Co-ordinates](images/map-coord.png)

+  Choose as many locations as you like, and add them to a two-dimensional list called `targets` in your Python script:

```python3
targets = [
  [52.205375, 0.119098],
  [52.202201, 0.128203]
]
```

Make sure you pick nearby locations, otherwise you'll find testing very difficult!
