# Software Installation

## Python Sense-Hat Libraries

To install the Sense-Hat software you need, run the following commands from a Terminal window:

```bash
sudo apt-get install sense-hat
sudo pip-3.2 install pillow
```

## Python piGPS library

1. There is a custom library created specifically for this resource, to use it you need to download it into the same directory as your project code. To do this run the following command from a Terminal window in the same directory as you project.

     ```bash
     wget https://goo.gl/fX1lsT -O piGPS.py
     ```

1. In order for the Sense-HAT to communicate with the GPS board you need to disable a service which will conflict with it. To do this you should enter this command at a Terminal.

    ```bash
    sudo systemctl disable serial-getty@ttyAMA0.service
    ```

1. You can then test your GPS board and software are working by running the piGPS python script.

    ```bash
    python3 piGPS.py
    ```

    The PiGPS program will try to establish a connection with some satelites and once it has it will output the current GPS data to the Terminal.

    `[0,0,0,0,0,0]` - means it is running but hasn't yet found any satelites.
    `[Time,Latitude,Londitude,Altitude,Satelites,GPS Fix]` - Is the data that will be displayed once satelites have been found.
