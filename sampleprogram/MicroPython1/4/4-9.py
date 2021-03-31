#!/usr/bin/env pybricks-micropython
from common import *

lmotor = Motor(Port.B)

# Lモーターの最大角速度
max_rotationalspeed = 1020

# モーターを最大角速度の50%で1秒間回転させ，ピタッと止める
lmotor.run_time(max_rotationalspeed*0.5, 1000, Stop.BRAKE)
wait(1000)

# モーターを最大角速度の50%で1秒間回転させ，ゆっくりと止める
lmotor.run_time(max_rotationalspeed*0.5, 1000, Stop.COAST)
wait(1000)