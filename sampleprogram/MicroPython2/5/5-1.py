#!/usr/bin/env pybricks-micropython
from common import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here
led_color = [Color.GREEN, Color.ORANGE]
touch_sensor = TouchSensor(Port.S1)

while True: #
    ev3.light.on(led_color[int(touch_sensor.pressed())])
    # waiting for 10 milliseconds
    wait(10)