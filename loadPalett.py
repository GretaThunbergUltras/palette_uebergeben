import brickpi3
import time


def readyfork(i):
    if i == 0:
        bp = brickpi3.BrickPi3()
        bp.set_motor_position(bp.PORT_C, -5000)
        bp.set_motor_position(bp.PORT_A, -2500)
    elif i == 1:
        bp = brickpi3.BrickPi3()
        bp.set_motor_position(bp.PORT_C, 0)
        bp.set_motor_position(bp.PORT_A, 0)


bp = brickpi3.BrickPi3()
readyfork(0)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, 20)
time.sleep(2)
bp.set_motor_power(bp.PORT_B, 0)
time.sleep(1)
readyfork(1)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, -18)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, 0)
time.sleep(2)

readyfork(0)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, -18)
time.sleep(2)
bp.set_motor_power(bp.PORT_B, 0)
time.sleep(1)
readyfork(1)
bp.set_motor_position(bp.PORT_D, 70)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, -30)
time.sleep(4)
bp.set_motor_power(bp.PORT_B, 0)
time.sleep(1)
bp.set_motor_position(bp.PORT_D, 0)
time.sleep(1)
bp.set_motor_position(bp.PORT_D, -60)
bp.set_motor_power(bp.PORT_B, 30)
time.sleep(4)
bp.set_motor_power(bp.PORT_B, 0)
bp.set_motor_position(bp.PORT_D, 0)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, 20)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, 0)


