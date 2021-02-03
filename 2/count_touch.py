#!/usr/bin/env pybricks-micropython
from common import *

touch_sensor = TouchSensor(Port.S1)

# 変数countを用意して0で初期化
count = 0

# countの値が3未満の間，繰り返す
while count < 3:
    # countの値を表示
    brick.display.text(str(count))
    
    # タッチセンサーが押されるまで繰り返す
    while not(touch_sensor.pressed()):
        wait(10)
    
    # タッチセンサーが離されるまで繰り返す
    while touch_sensor.pressed():
        wait(10)

    # countを+1
    count = count + 1

# 音量50で500ミリ秒間，ド（262Hz）の音を鳴らす
brick.sound.beep(262, 500, 50)
