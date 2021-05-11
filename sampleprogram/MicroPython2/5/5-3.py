#!/usr/bin/env pybricks-micropython
from common import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
color_sensor = ColorSensor(Port.S3)

while True: #
    b_color = Color.ORANGE if color_sensor.ambient() > 10 else Color.GREEN
    ev3.light.on(b_color)
    # waiting for 10 milliseconds
    wait(10)