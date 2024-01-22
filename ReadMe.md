# 运行

```
rosrun grpc_ros robot_server.py
python3 robot_client.py
```

# 安装grpc-python
```
pip3 install grpcio -i https://pypi.tuna.tsinghua.edu.cn/simple 
pip3 install grpcio-tools -i https://pypi.tuna.tsinghua.edu.cn/simple 
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. robot_data.proto
``