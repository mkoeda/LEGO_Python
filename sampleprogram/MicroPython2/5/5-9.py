#!/usr/bin/env pybricks-micropython
from common import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
motor = Motor(Port.B)

# Initialize a motor (by default this means clockwise, without any gears).
motor.reset_angle(0)
motor.stop()

while True: #
    b_color = Color.ORANGE if motor.angle() > 90 else Color.GREEN
    ev3.light.on(b_color)
    # waiting for 10 milliseconds
    wait(10)