#!/usr/bin/env pybricks-micropython
from common import *

# 2秒間，緑色に点灯する
brick.light(Color.GREEN)
wait(2000)

# 2秒間，オレンジ色に点灯する
brick.light(Color.ORANGE)
wait(2000)

# 2秒間，赤色に点灯する
brick.light(Color.RED)
wait(2000)

# 消す
brick.light(None)
