#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

ultrasonic_sensor = UltrasonicSensor(Port.S4)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.drive(50, 0)

while True:
    if ultrasonic_sensor.distance() < 500 :
        break

robot.stop(Stop.BRAKE)
wait(1000)