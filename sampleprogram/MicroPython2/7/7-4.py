#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

# 左右のモーターのインスタンス
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# タイヤの直径，mm単位
wheel_diameter = 56
# 左右のタイヤ間の距離 mm単位
axle_track = 123

# ロボットのインスタンス
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# 関数forward_doremiの定義
def forward_doremi(pow, ste):
    # 前進速度 pow mm/s，回転角速度 ste deg/sで1000ミリ秒間だけ移動
    robot.drive(pow, ste)
    wait(1000)
    robot.stop()

    # 音量100で200ミリ秒間ずつ，ドレミの音を鳴らす
    ev3.speaker.set_volume(100)
    ev3.speaker.beep(262, 200)
    ev3.speaker.beep(294, 200)
    ev3.speaker.beep(330, 200)

# 関数forward_doremiの呼び出し
forward_doremi(200, 100)
