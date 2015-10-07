##### Libraries #####
from sense_hat import SenseHat
from time import sleep
from random import random

##### Functions #####


##### Pixel Art #####
r = (255, 0, 0)
g = (0, 255, 0)
w = (255, 255, 255)
e = (0, 0, 0)

locked = [e,e,e,e,e,e,e,e,e,e,e,w,w,e,e,e,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,e,e,r,r,r,r,e,e,e,e,r,r,r,r,e,e,e,e,r,r,r,r,e,e,e,e,e,e,e,e,e,e]

unlocked = [e,e,e,e,e,e,e,e,e,e,e,e,e,w,w,e,e,e,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,g,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,e,e,e,e,e,e]


##### Main Program #####
sense = SenseHat()
sense.set_pixels(locked)
sleep(2)

##### Locks #####

## Temperature Lock ##
current_temp=sense.get_temperature()
difference = random()*5
difference = round(difference,1)
target_temp=current_temp+difference

print(current_temp,target_temp)
sleep(3)
while abs(difference) > 0.1:
    current_temp = sense.get_temperature()
    print(difference)
    difference = target_temp - current_temp
    if difference > 0:
        sense.clear(0,0,255)
    else:
        sense.clear(255,0,0)
    



##### Unlocked #####
sense.set_pixels(unlocked)
sleep(2)
sense.show_message("This is a secret message",scroll_speed=0.05,text_colour=(255,0,0))
