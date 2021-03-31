#!/usr/bin/env pybricks-micropython
from common import *

ultrasonic_sensor = UltrasonicSensor(Port.S1)

while True:
    b_color = Color.ORANGE if ultrasonic_sensor.distance() > 500 else Color.GREEN
    brick.light(b_color)
    wait(10)
