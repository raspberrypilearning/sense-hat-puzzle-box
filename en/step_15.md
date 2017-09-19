## Location Lock

In order for your Raspberry Pi to know its location, it will need to use a technology known as GPS (Global Positioning System), which uses communication with satellites to determine a position.

Your Raspberry Pi will need to communicate with at least four GPS satellites to get an accurate location. By timing the speed of this communication, the distance from each satellite can be calculated. Once we know the distance to all four satellites, a 3D position on Earth can be given in terms of:

  - **Latitude**, the distance north or south of the Equator. Positive distances are north and negative distances are south.
  - **Longitude**, the distance east or west of the Greenwich Prime Meridian in London. Positive distances are east and negative distances are west.
  - **Altitude**, the current height above sea level.

You'll need to add GPS functionality to your Raspberry Pi. This can be done in a number of ways but we used a GPS USB stick like [this one](https://www.amazon.co.uk/Diymall-G-mouse-Glonass-Raspberry-Aviation/dp/B015E2XSSO).

Ensure you have installed the **piGPS** library before continuing.

### How will the lock work?

The lock will work as follows:

- Create a `gps` object which continually checks for GPS data.
- Set up a list of destination(s) which the user must visit.
- Calculate the distance of the Raspberry Pi from the first target location
- Continually check the distance to the target location until you are within 10m of it. It then tells you whether you are getting closer or further away.
- Once all the target destinations have been visited the program will give an indication that the location lock is unlocked.
