#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

motor = Motor(Port.B)

motor.reset_angle(0)
motor.stop()

while True:
    b_color = Color.ORANGE if motor.angle() > 90 else Color.GREEN
    ev3.light.on(b_color)
    wait(10)