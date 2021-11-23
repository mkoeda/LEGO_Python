#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

led_color = [Color.GREEN, Color.ORANGE]
touch_sensor = TouchSensor(Port.S1)

while True:
    ev3.light.on(led_color[int(touch_sensor.pressed())])
    wait(10)