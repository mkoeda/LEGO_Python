#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

# 画面を消す
ev3.screen.clear()

# helloとev3!をそれぞれ(10,10), (10, 20)の座標に5秒間表示する
ev3.screen.draw_text(10, 10, 'hello')
ev3.screen.draw_text(10, 20, 'ev3!')
wait(5000)

# 画面を消す
ev3.screen.clear()

# hello python!を2行で5秒間表示する
ev3.screen.print('hello')
ev3.screen.print('python!')
wait(5000)
