#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

# 2秒間，緑色に点灯する
ev3.light.on(Color.GREEN)
wait(2000)

# 2秒間，オレンジ色に点灯する
ev3.light.on(Color.ORANGE)
wait(2000)

# 2秒間，赤色に点灯する
ev3.light.on(Color.RED)
wait(2000)

# 消す
ev3.light.off()
