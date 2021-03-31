#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

# ボタン入力待ち
while not any(ev3.buttons.pressed()):
    wait(10)

ev3.speaker.set_volume(100)
ev3.speaker.beep()
