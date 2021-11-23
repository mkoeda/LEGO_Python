#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

color_sensor = ColorSensor(Port.S3)

while True:
    b_color = Color.ORANGE if color_sensor.ambient() > 10 else Color.GREEN
    ev3.light.on(b_color)
    wait(10)