#!/usr/bin/env pybricks-micropython
from common import *

ultrasonic_sensor = UltrasonicSensor(Port.S4)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 114)

robot.drive(50, 0)

while True:
    if ultrasonic_sensor.distance() < 500 :
        break

robot.stop(Stop.BRAKE)