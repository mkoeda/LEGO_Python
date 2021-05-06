#!/usr/bin/env pybricks-micropython
from common import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here
gyro_sensor = GyroSensor(Port.S2)

# Initialize two motors and a drive base
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

gyro_sensor.reset_angle(0)

# Drive forward /speed:0 steering: 45 [deg/s] /
robot.drive(0, 45)

# Wait until the gyro sensor detects that the robot has turned
while True: #
    if gyro_sensor.angle() > 90 :
        break
#
robot.stop(Stop.BRAKE)
wait(1000)