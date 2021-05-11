#!/usr/bin/env pybricks-micropython
from common import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
touch_sensor = TouchSensor(Port.S1)

# Initialize two motors and a drive base
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Drive forward /speed:50 steering:0/
robot.drive(50, 0)

while not touch_sensor.pressed(): # while touch sensor is not pressed
    # waiting for 10 milliseconds
    wait(10)
#
robot.stop(Stop.BRAKE)

wait(1000)