#!/usr/bin/env pybricks-micropython
from common import *
import math

# 左右のモーターのインスタンス
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# タイヤの直径，mm単位
wheel_diameter = 56
# 左右のタイヤ間の距離 mm単位
axle_track = 123

# ロボットのインスタンス
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

#  100mm/sで1000ミリ秒間だけ前進
robot.drive_time(100, 0, 1000)
# 100mm/sで1000ミリ秒間だけ後退
robot.drive_time(-100, 0, 1000)

# 90deg/sで1000ミリ秒間だけ右にスピンターン
robot.drive_time(0, 90, 1000)
# 90deg/sで1000ミリ秒間だけ左にスピンターン
robot.drive_time(0, -90, 1000)

# ロボットの角速度
pivot = 45
# 右タイヤ中心に角速度pivotで2000ミリ秒間ピボットターン
robot.drive_time(math.pi * axle_track * pivot / 360, pivot, 2000)
# 左タイヤ中心に角速度pivotで2000ミリ秒間ピボットターン
robot.drive_time(math.pi * axle_track * pivot / 360, -pivot, 2000)