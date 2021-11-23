#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

touch_sensor = TouchSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.drive(50, 0)

while not touch_sensor.pressed():
    wait(10)

robot.stop(Stop.BRAKE)
wait(1000)