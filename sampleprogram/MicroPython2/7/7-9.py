#!/usr/bin/env pybricks-micropython
from common import *
import time

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diameter = 56
axle_track =123
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

color_sensor = ColorSensor(Port.S3)

lines = 0
robot.drive(100, 0)

t0 = time.time()

while time.time()-t0 < 30:
    output = str(lines) + 'lines'
    ev3.screen.clear()
    ev3.screen.draw_text(0, 40, output)
    while True:
        if color_sensor.color() == Color.BLACK:
            break
    while True:
        if color_sensor.color() == Color.WHITE:
            break

    lines = lines + 1

robot.stop(Stop.BRAKE)
