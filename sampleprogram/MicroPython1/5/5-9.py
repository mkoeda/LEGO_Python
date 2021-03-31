#!/usr/bin/env pybricks-micropython
from common import *

motor = Motor(Port.B)

motor.reset_angle(0)
motor.stop(Stop.COAST)

while True:
    b_color = Color.ORANGE if motor.angle() > 90 else Color.GREEN
    brick.light(b_color)
    wait(10)