# -*- coding: utf-8 -*-
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
import time
import datetime
import numpy as np
import cv2

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = robot_data_pb2_grpc.RobotStub(channel)
        height = 480
        width = 640
        # while True:
        for img_data in stub.GetHeadCamImage(robot_data_pb2.Empty()):
            if img_data is not None:
                print("time:", img_data.time.decode('utf-8','ignore'))
                img = np.frombuffer(img_data.image_data, dtype=np.uint8).reshape(height, width, -1)
                # rbg to bgr
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                cv2.imshow("Image", img)
                cv2.waitKey(1)
        
if __name__ == '__main__':
    run()
