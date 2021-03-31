#!/usr/bin/env pybricks-micropython
from common import *
import _thread

# 左右のモーターのインスタンス
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# タイヤの直径，mm単位
wheel_diameter = 56
# 左右のタイヤ間の距離 mm単位
axle_track = 123

# ロボットのインスタンス
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# 超音波センサーのインスタンス
us_sensor = UltrasonicSensor(Port.S4)

# 壁に近づいたかを表すフラグ
flg = 0

# 超音波センサーの値を取得して比較する関数
def check_distance():
    global flg
    while True:
        # distanceの値を表示
        distance = us_sensor.distance()
        brick.display.text(str(distance))

        if distance < 50:            
            break
    flg = 1
    return

# スレッドの開始
_thread.start_new_thread(check_distance, ())

# ロボットを前進させ続け，壁に近づいたら止める
robot.drive(100, 0)
while True:
    if flg == 1:
        break
robot.stop()
