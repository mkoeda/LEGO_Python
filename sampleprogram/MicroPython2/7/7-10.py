#!/usr/bin/env pybricks-micropython

from common import *

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diameter = 56
axle_track =123
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

color_sensor_1 = ColorSensor(Port.S3)
color_sensor_2 = ColorSensor(Port.S2)

while True:
    if color_sensor_2.color() == Color.BLACK:
        break

    if color_sensor_1.color() == Color.BLACK:
        robot.drive(50, 30)
    else:
        robot.drive(50, -30)

robot.stop(Stop.BRAKE)
robot.turn(90)