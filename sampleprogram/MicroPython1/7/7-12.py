#!/usr/bin/env pybricks-micropython

from common import *
import _thread

flg = 0

def detect_line(m, cs, lk):
    global flg
    m.run(360)
    while True:
        if cs.color() == Color.BLACK:
            break
    m.stop(Stop.BRAKE)
    lk.acquire()
    flg = flg + 1
    lk.release()
    return


left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

left_color_sensor = ColorSensor(Port.S2)
right_color_sensor = ColorSensor(Port.S3)

lock = _thread.allocate_lock()
_thread.start_new_thread(detect_line, (left_motor, left_color_sensor, lock))
_thread.start_new_thread(detect_line, (right_motor, right_color_sensor, lock))

while flg < 2:
    pass

wheel_diameter = 56
axle_track =123
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

robot.drive_time(0, 180, 500)
