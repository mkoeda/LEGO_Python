#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

ultrasonic_sensor = UltrasonicSensor(Port.S4)

while True:
    b_color = Color.ORANGE if ultrasonic_sensor.distance() > 500 else Color.GREEN
    ev3.light.on(b_color)
    wait(10)