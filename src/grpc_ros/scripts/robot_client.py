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

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = robot_data_pb2_grpc.RobotStub(channel)
        while True:
            print("---------------------------------------------\n")
            print("Calling GetCarData...")
            response = stub.GetCarData(robot_data_pb2.Empty())
            print("Power Voltage:", response.power_voltage)
            print("Temperature:", response.temperature)
            print("Smoke:", response.smoke)
            print("Is Charging:", response.is_charge)
            print("Speed - X:", response.speed.x)
            print("Speed - Y:", response.speed.y)
            print("Speed - Angular:", response.speed.angular)
            print("Position - X:", response.position.x)
            print("Position - Y:", response.position.y)
            print("Orientation - X:", response.orientation.x)
            print("Orientation - Y:", response.orientation.y)
            print("Orientation - Z:", response.orientation.z)
            print("Orientation - W:", response.orientation.w)

            print("\nCalling GetFaceResult...")
            # 调用 GetYoloResult 接口
            response = stub.GetYoloResult(robot_data_pb2.Empty())
            # 打印结果
            print("Yolo Result:")
            for box in response.boxs:
                print(f"Box {box.id}: x1={box.x1}, y1={box.y1}, x2={box.x2}, y2={box.y2}, label={box.label}, conf={box.conf}")
            print("Time:", response.time)
            time.sleep(1)

if __name__ == '__main__':
    run()
