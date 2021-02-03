#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick

freq = [262, 294, 330]
for i in range(3):
    brick.sound.beep(freq[i], 500, 20)

# hogehoge