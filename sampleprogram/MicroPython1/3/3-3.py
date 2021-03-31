#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

wheel_diameter = 56
axle_track =123

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

robot.drive_time(200, 0, 2000)
