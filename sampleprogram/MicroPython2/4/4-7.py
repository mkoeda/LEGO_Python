#!/usr/bin/env pybricks-micropython
from common import *

lmotor = Motor(Port.B)

# Lモーターの最大角速度
max_rotationalspeed = 1020

# モーターを最大角速度の50%で1回転（360度回転）させ，ピタッと止める
lmotor.run_angle(max_rotationalspeed*0.5, 360, Stop.BRAKE)
wait(1000)

# モーターを最大角速度の50%で1回転（360度回転）させ，ゆっくりと止める
lmotor.run_angle(max_rotationalspeed*0.5, 360, Stop.COAST)
wait(1000)