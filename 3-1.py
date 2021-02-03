#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

Motor(Port.B).run(360)
Motor(Port.C).run(360)

wait(2000)

Motor(Port.B).stop(Stop.BRAKE)
Motor(Port.C).stop(Stop.BRAKE)
