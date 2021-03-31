#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import wait

# ボタン入力待ち
while not any(brick.buttons()):
    wait(10)

brick.sound.beep()