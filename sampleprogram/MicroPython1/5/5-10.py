#!/usr/bin/env pybricks-micropython
from common import *

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 114)

left_motor.reset_angle(0)

robot.drive(50, 0)

while True:
    if left_motor.angle() > 360 :
       break
    wait(10)

robot.stop(Stop.BRAKE)