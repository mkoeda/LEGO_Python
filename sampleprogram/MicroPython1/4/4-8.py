#!/usr/bin/env pybricks-micropython
from common import *

lmotor = Motor(Port.B)

# Lモーターの最大角速度
max_rotationalspeed = 1020

# 回転数
rotation = 1

# モーターを最大角速度の50%で1回転させ，ピタッと止める
lmotor.run_angle(max_rotationalspeed*0.5, 360*rotation, Stop.BRAKE)
wait(1000)

# モーターを最大角速度の50%で1回転させ，ゆっくりと止める
lmotor.run_angle(max_rotationalspeed*0.5, 360*rotation, Stop.COAST)
wait(1000)