#!/usr/bin/env pybricks-micropython
from common import *

#駆動歯車数 36, 従動歯車数 12の場合
geared_motor = Motor(Port.A, Direction.CLOCKWISE, [36, 12])

#駆動歯車数 12, 従動歯車数 36の場合
#geared_motor = Motor(Port.A, Direction.CLOCKWISE, [12, 36])

#回転速度 100 deg/s で， 90 度回転させる
geared_motor.run_angle(100,90)