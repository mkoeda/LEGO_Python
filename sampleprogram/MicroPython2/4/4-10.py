#!/usr/bin/env pybricks-micropython
from common import *

# 左右のモーターのインスタンス
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# タイヤの直径，mm単位
wheel_diameter = 56
# 左右のタイヤ間の距離 mm単位
axle_track = 123

# ロボットのインスタンス
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# 直進速度[mm/s]，直進加速度[mm/s/s]，回転角速度[deg/s]，回転角加速度[deg/s/s]を設定
robot.settings(100, 100, 100, 100)

#  100mm前進
robot.straight(100)
#  100mm後退
robot.straight(-100)


# 右に90degスピンターン
robot.turn(90)
# 左に90degスピンターン
robot.turn(-90)
