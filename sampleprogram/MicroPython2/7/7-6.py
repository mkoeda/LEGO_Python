#!/usr/bin/env pybricks-micropython
from common import *
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diameter = 56
axle_track =123
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

color_sensor = ColorSensor(Port.S3)

t0 = time.time()

while time.time()-t0 < 10:
    if color_sensor.reflection() <= 50 :
        robot.drive(50, 30)
    else:
        robot.drive(50, -30)
