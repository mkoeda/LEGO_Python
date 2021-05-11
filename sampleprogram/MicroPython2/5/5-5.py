#!/usr/bin/env pybricks-micropython
from common import *

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
gyro_sensor = GyroSensor(Port.S2)

while True: #
    b_color = Color.ORANGE if gyro_sensor.speed() > 90 else Color.GREEN
    ev3.light.on(b_color)
    # waiting for 10 milliseconds
    wait(10)