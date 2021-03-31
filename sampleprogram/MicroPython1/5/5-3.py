#!/usr/bin/env pybricks-micropython
from common import *

color_sensor = ColorSensor(Port.S3)

while True:
    b_color = Color.ORANGE if color_sensor.ambient() > 10 else Color.GREEN
    brick.light(b_color)
    wait(10)
