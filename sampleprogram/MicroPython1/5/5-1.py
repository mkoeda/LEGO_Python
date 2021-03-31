#!/usr/bin/env pybricks-micropython
from common import *

led_color = [Color.GREEN, Color.ORANGE]
touch_sensor = TouchSensor(Port.S1)

while True:
    brick.light(led_color[int(touch_sensor.pressed())])
    wait(10)
