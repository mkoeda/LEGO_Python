#!/usr/bin/env pybricks-micropython
from common import *

gyro_sensor = GyroSensor(Port.S2)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 114)

gyro_sensor.reset_angle(0)

robot.drive(0, 45)

while True:
    if gyro_sensor.angle() > 90 :
       break

robot.stop(Stop.BRAKE)