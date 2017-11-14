## Location lock

To program this lock, you'll need to add GPS functionality to your Raspberry Pi. This can be done in a number of ways, but we used a GPS USB device like [this one](https://www.amazon.co.uk/Diymall-G-mouse-Glonass-Raspberry-Aviation/dp/B015E2XSSO).

**Note**: if you do not have a GPS device, skip ahead to the final step of the project.

Ensure you have installed the `piGPS` library before continuing — see step 2 if you still need to install it.

### GPS

In order for your Raspberry Pi to find out its location on Earth, it will need to use communication with satellites via the technology known as GPS (Global Positioning System).

Your Raspberry Pi will have to communicate with at least four GPS satellites to get an accurate location. By timing the speed of this communication, it can calculate its distance from each satellite. Once it knows the distance to all four satellites, it can determine its position on this planet in terms of:

  - **Latitude**, the position north or south of the equator (positive latitude values are north and negative latitude values are south)
  - **Longitude**, the position east or west of the Greenwich Prime Meridian in London (positive longitude values are east and negative longitude values are west)
  - **Altitude**, the height above sea level

### How will the lock work?

You will write the code for the lock using the following steps:

- Create a `gps` object which continually checks for GPS data
- Set up a list of destination(s) which the user must visit
- Calculate the distance of the Raspberry Pi from the first target location
- Continually check the distance to the target location until the Raspberry Pi is within 10 m of it, then tell the user whether they are getting closer or further away
- Once all the target destinations have been visited, the program will tell the user that the location lock has opened
