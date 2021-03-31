#!/usr/bin/env pybricks-micropython

from common import *
import _thread

color_sensor_1 = ColorSensor(Port.S3)
color_sensor_2 = ColorSensor(Port.S2)

flg = 0

def detect_line():
    global flg
    while True:
        if color_sensor_2.color() == Color.BLACK:
            flg = 1
            break
    return


left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diameter = 56
axle_track =123
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

_thread.start_new_thread(detect_line, ())

while flg == 0:
    if color_sensor_1.color() == Color.BLACK:
        robot.drive(50, 30)
    else:
        robot.drive(50, -30)

robot.stop(Stop.BRAKE)
robot.drive_time(0, 180, 500)
