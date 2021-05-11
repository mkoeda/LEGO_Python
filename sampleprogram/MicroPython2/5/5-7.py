#!/usr/bin/env pybricks-micropython
from common import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here
ultrasonic_sensor = UltrasonicSensor(Port.S4)

while True: #
    b_color = Color.ORANGE if ultrasonic_sensor.distance() > 500 else Color.GREEN
    ev3.light.on(b_color)
    # waiting for 10 milliseconds
    wait(10)