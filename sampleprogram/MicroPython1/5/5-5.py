#!/usr/bin/env pybricks-micropython
from common import *

gyro_sensor = GyroSensor(Port.S2)

while True:
    b_color = Color.ORANGE if gyro_sensor.speed() > 90 else Color.GREEN
    brick.light(b_color)
    wait(10)