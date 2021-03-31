#!/usr/bin/env pybricks-micropython
from common import *
import time

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diameter = 56
axle_track =123
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

color_sensor = ColorSensor(Port.S3)

KP = 2.0
KD = 0.5
target = 50

p_error = 0
t0 = time.time()

while time.time()-t0 < 30:
    bright = color_sensor.reflection()
    error = target - bright
    turn = error * KP + (error - p_error) * KD

    robot.drive(70, turn)
    p_error = error
