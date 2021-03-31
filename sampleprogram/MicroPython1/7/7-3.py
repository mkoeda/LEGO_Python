#!/usr/bin/env pybricks-micropython
from common import *
import random

# 左右のモーターのインスタンス
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# タイヤの直径，mm単位
wheel_diameter = 56
# 左右のタイヤ間の距離 mm単位
axle_track = 123

# ロボットのインスタンス
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

for n in range(5):
    # -100～100の乱数を発生させる
    steering = random.randrange(-100, 100)
    # 前進速度100mm/s，回転角速度steeringで1000ミリ秒間だけ移動
    robot.drive_time(100, steering, 1000)