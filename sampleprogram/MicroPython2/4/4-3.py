#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

# 音量100% に設定する
ev3.speaker.set_volume(100)

# 周波数2000Hz, 2000ミリ秒間, 音を鳴らす
ev3.speaker.beep(2000, 2000)
