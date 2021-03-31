#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

touch_sensor = TouchSensor(Port.S1)

# 変数countを用意して0で初期化
count = 0

# 音量を50%に設定
ev3.speaker.set_volume(50)

# countの値が3未満の間，繰り返す
while count < 3:
    # countの値を表示
    ev3.screen.print(str(count))
    
    # タッチセンサーが押されるまで繰り返す
    while not(touch_sensor.pressed()):
        wait(10)
    
    # タッチセンサーが離されるまで繰り返す
    while touch_sensor.pressed():
        wait(10)

    # countを+1
    count = count + 1

# 音を鳴らす
ev3.speaker.beep()
