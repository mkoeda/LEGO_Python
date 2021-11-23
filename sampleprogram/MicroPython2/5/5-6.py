#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

gyro_sensor = GyroSensor(Port.S2)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

gyro_sensor.reset_angle(0)

robot.drive(0, 45)

while True:
    if gyro_sensor.angle() > 90 :
        break

robot.stop(Stop.BRAKE)
wait(1000)