#!/usr/bin/env pybricks-micropython
from common import *

touch_sensor = TouchSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 114)

robot.drive(50, 0)

while not touch_sensor.pressed():
    wait(10)

robot.stop(Stop.BRAKE)
