#!/usr/bin/env pybricks-micropython
from common import *

color_sensor = ColorSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.drive(50, 0)

while True:
    if color_sensor.reflection() < 10 :
        break

robot.stop(Stop.BRAKE)
wait(1000)