#! /usr/bin/env python3
#coding=utf-8
import rospy
from std_msgs.msg import String
from rei_robot_base.msg import CarData
from nav_msgs.msg import Odometry
from concurrent import futures
import grpc
import os
import sys
# 获取当前脚本所在目录的绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(current_dir, '..', 'rpc'))
# 将项目根目录添加到sys.path
sys.path.append(project_root)
import robot_data_pb2
import robot_data_pb2_grpc
# from rpc import robot_data_pb2
# from rpc import robot_data_pb2_grpc
from grpc_ros.msg import yolo
from face_rec.msg import face_data
# from grpc_ros.msg import Box
from datetime import datetime

SERVER_ADDRESS = "localhost:50051"

class RobotServicer(robot_data_pb2_grpc.Robot):
    def __init__(self):
        self.speed = [0.0, 0.0, 0.0]
        self.position = [0.0, 0.0] # 位置 x, y
        self.orientation = [0.0, 0.0, 0.0, 0.0] # 朝向 x, y, z, w
        self.power_voltage = 0 # 电量
        self.temperature = 0
        self.relative_humidity = 0
        self.smoke = -1
        self.is_charge = False

        self.yolo_result = None
        self.yolo_img_shape = None
        self.yolo_result_class_names = None
        self.yolo_result_time = ''

        self.face_result = None
        self.face_result_time = ''

        self.car_data_subscriber = rospy.Subscriber('car_data', CarData, self.cat_data_topic_callback) # 订阅car_data话题
        self.odom_subscriber = rospy.Subscriber('odom', Odometry, self.odom_topic_callback) # 订阅odom话题
        if rospy.has_param('/robot_server/yolo_result_topic'):
            yolo_result_topic = rospy.get_param('/robot_server/yolo_result_topic')
        else:
            yolo_result_topic = 'yolo_result'
        self.yolo_result_subscriber = rospy.Subscriber(yolo_result_topic, yolo, self.yolo_result_topic_callback) # 订阅yolo_result话题

        self.face_result_subscriber = rospy.Subscriber('face_results', face_data, self.face_result_topic_callback) # 订阅face_result话题

    # car_data回调函数
    def cat_data_topic_callback(self, msg):
        self.power_voltage = msg.power_voltage
        self.temperature = msg.tempareture
        self.relative_humidity = msg.relative_humidity
        self.smoke = msg.smoke
        self.is_charge = msg.is_charge

    # odom回调函数
    def odom_topic_callback(self, msg):
        self.speed[0] = msg.twist.twist.linear.x
        self.speed[1] = msg.twist.twist.linear.y
        self.speed[2] = msg.twist.twist.angular.z
        self.position[0] = msg.pose.pose.position.x
        self.position[1] = msg.pose.pose.position.y
        self.orientation[0] = msg.pose.pose.orientation.x
        self.orientation[1] = msg.pose.pose.orientation.y
        self.orientation[2] = msg.pose.pose.orientation.z
        self.orientation[3] = msg.pose.pose.orientation.w

    # 重写rpc接口，返回car_data数据
    def GetCarData(self, request, context):
        speed = robot_data_pb2.CarData.Speed()
        speed.x = self.speed[0]
        speed.y = self.speed[1]
        speed.angular = self.speed[2]
        position = robot_data_pb2.CarData.Position()
        position.x = self.position[0]
        position.y = self.position[1]
        orientation = robot_data_pb2.CarData.Orientation()
        orientation.x = self.orientation[0]
        orientation.y = self.orientation[1]
        orientation.z = self.orientation[2]
        orientation.w = self.orientation[3]
        car_data = robot_data_pb2.CarData(
            power_voltage=self.power_voltage,
            temperature=self.temperature,
            smoke=self.smoke,
            is_charge=self.is_charge,
            speed=speed,
            position=position,
            orientation=orientation
        )
        return car_data
    
    # yolo_result回调函数
    def yolo_result_topic_callback(self, msg):
        # 将 boxes 消息中的数据提取到 self.yolo_result
        self.yolo_result = []

        # 遍历每个 Box，将其信息添加到 self.yolo_result
        for box_data in msg.boxes:
            box_info = {
                'x1': box_data.x1,
                'y1': box_data.y1,
                'x2': box_data.x2,
                'y2': box_data.y2,
                'conf': box_data.conf,
                'cls': box_data.cls,
                'id': box_data.id
            }
            self.yolo_result.append(box_info)
        
        if len(self.yolo_result) == 0:
            self.yolo_result = None
            return

        # 如果需要，还可以处理 shape 和 class_names 字段
        self.yolo_img_shape = (msg.shape[0], msg.shape[1])
        self.yolo_result_class_names = msg.class_names
        # 设置 self.yolo_result_time
        self.yolo_result_time = self.ros_time_to_string(msg.header.stamp)

    # 将ros_time转换为年月日时分秒的字符串格式
    def ros_time_to_string(self, stamp):
        # 将时间戳转换为秒和纳秒
        seconds = stamp.secs
        nanoseconds = stamp.nsecs
        
        # 将秒转换为日期和时间
        dt = datetime.fromtimestamp(seconds)
        year = dt.year
        month = dt.month
        day = dt.day
        hour = dt.hour
        minute = dt.minute
        second = dt.second
        # millisecond = nanoseconds / 1e6  # 毫秒
        # 将日期和时间转换为字符串
        date_time = f'{year}-{month}-{day} {hour}:{minute}:{second}.{nanoseconds}'
        return date_time
    
    # 重写rpc接口，返回yolo_result数据
    def GetYoloResult(self, request, context):
        # 如果 self.yolo_result 为 None，返回一个空的 YoloResult 消息
        if self.yolo_result is None:
            return robot_data_pb2.YoloResult()

        # 构建 YoloResult 消息
        yolo_result = robot_data_pb2.YoloResult()

        # 遍历每个 Box，并将其添加到 YoloResult 消息中
        for box_data in self.yolo_result:
            box_msg = yolo_result.boxs.add()
            box_msg.x1 = box_data['x1']
            box_msg.y1 = box_data['y1']
            box_msg.x2 = box_data['x2']
            box_msg.y2 = box_data['y2']
            # box_msg.label = str(box_data['cls'])
            box_msg.label = self.yolo_result_class_names[box_data['cls']]
            box_msg.conf = box_data['conf']
            box_msg.id = box_data['id']

        # 设置 YoloResult 的 time 字段（如果有的话）
        yolo_result.time = self.yolo_result_time.encode('utf-8')

        # 清除yolo_result
        self.yolo_result = None
        self.yolo_result_time = ''
        return yolo_result
    
    # face_result回调函数
    def face_result_topic_callback(self, msg):
        # 将 boxes 消息中的数据提取到 self.yolo_result
        self.face_result = []

        # 遍历每个 Box，将其信息添加到 self.yolo_result
        for face_data in msg.faces:
            face_info = {
                'x1': face_data.xmin,
                'y1': face_data.ymin,
                'x2': face_data.xmax,
                'y2': face_data.ymax,
                'name': face_data.name
            }
            self.face_result.append(face_info)
        
        if len(self.face_result) == 0:
            self.face_result = None
            return

        # 设置 self.yolo_result_time
        self.face_result_time = str(datetime.datetime.now())

    # 重写rpc接口，返回face_result数据
    def GetFaceResult(self, request, context):
        if self.face_result is None:
            return robot_data_pb2.FaceResult()
        # 遍历每个face_result，并将其添加到FaceResult消息中
        face_result = robot_data_pb2.FaceResult()
        for face_data in self.face_result:
            face_msg = face_result.faces.add()
            face_msg.x1 = face_data['x1']
            face_msg.y1 = face_data['y1']
            face_msg.x2 = face_data['x2']
            face_msg.y2 = face_data['y2']
            face_msg.name = face_data['name']

        face_result.time = self.face_result_time.encode('utf-8')
        self.face_result = None
        self.face_result_time = ''
        return face_result


def serve():
    # 打印使用说明
    print("Usage:")
    print("rosrun grpc_ros robot_server.py")
    print("rosrun grpc_ros robot_server.py _yolo_result_topic:=/yolo_result")
    print("rosrun grpc_ros robot_server.py _yolo_result_topic:=/yolov8_trt/result")
    print("---------------------------------------------")
    rospy.init_node('robot_server')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    robot_data_pb2_grpc.add_RobotServicer_to_server(RobotServicer(), server)
    server.add_insecure_port(SERVER_ADDRESS)
    server.start()
    print("server listen on ", SERVER_ADDRESS)
    rospy.spin()

if __name__ == '__main__':
    serve()
