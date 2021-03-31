#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

left_motor.run(360)
right_motor.run(360)

wait(2000)

left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)
