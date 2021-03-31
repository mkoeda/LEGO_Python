#!/usr/bin/env pybricks-micropython
from common import *

color_sensor = ColorSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 114)

robot.drive(50, 0)

while True:
    if color_sensor.reflection() < 10 :
        break

robot.stop(Stop.BRAKE)