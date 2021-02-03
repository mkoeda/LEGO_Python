#!/usr/bin/env pybricks-micropython
from common import *

# 画面を消す
brick.display.clear()

# hello ev3!を2行で5秒間表示する
brick.display.text('hello', (10, 10))
brick.display.text('ev3!', (10, 20))
wait(5000)

# 画面を消す
brick.display.clear()

# hello python!を2行で5秒間表示する
# 座標を指定を省略すると画面の上側から一行ずつ自動的に配置される
brick.display.text('hello')
brick.display.text('python!')
wait(5000)
