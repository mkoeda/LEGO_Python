#!/usr/bin/env pybricks-micropython
from common import *

ev3 = EV3Brick()

# 音量100% に設定する
ev3.speaker.set_volume(100)

# C4の音を鳴らす
ev3.speaker.play_notes(['C4/4'])
# D4の音を鳴らす
ev3.speaker.play_notes(['D4/4'])
# E4の音を鳴らす
ev3.speaker.play_notes(['E4/4'])
# F4の音を鳴らす
ev3.speaker.play_notes(['F4/4'])
# G4の音を鳴らす
ev3.speaker.play_notes(['G4/4'])
