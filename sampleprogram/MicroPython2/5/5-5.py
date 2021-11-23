#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

gyro_sensor = GyroSensor(Port.S2)

while True:
    b_color = Color.ORANGE if gyro_sensor.speed() > 90 else Color.GREEN
    ev3.light.on(b_color)
    wait(10)