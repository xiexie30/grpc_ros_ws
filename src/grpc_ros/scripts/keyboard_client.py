#!/usr/bin/env python
from __future__ import print_function

import os
import sys
import grpc
# 获取当前脚本所在目录的绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(current_dir, '..', 'rpc'))
# 将项目根目录添加到sys.path
sys.path.append(project_root)
import robot_data_pb2
import robot_data_pb2_grpc


from select import select

if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    import tty


msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

def getKey(settings, timeout):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        rlist, _, _ = select([sys.stdin], [], [], timeout)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def saveTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)

def restoreTerminalSettings(old_settings):
    if sys.platform == 'win32':
        return
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)


if __name__=="__main__":
    settings = saveTerminalSettings()

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = robot_data_pb2_grpc.RobotStub(channel)
        while True:
            key = getKey(settings, 0.5)
            if key == '':
                continue
            if key == '\x03':
                break
            message = robot_data_pb2.Keyboard()
            message.key = str(key)
            response = stub.SetTwistKeyboard(message)
            print(response)

    restoreTerminalSettings(settings)