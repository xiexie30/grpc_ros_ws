# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10robot_data.proto\x12\x05robot\"\x07\n\x05\x45mpty\"\x80\x03\n\x07\x43\x61rData\x12\x15\n\rpower_voltage\x18\x01 \x01(\x02\x12\x13\n\x0btemperature\x18\x02 \x01(\x02\x12\x19\n\x11relative_humidity\x18\x03 \x01(\x02\x12\r\n\x05smoke\x18\x04 \x01(\x05\x12\x11\n\tis_charge\x18\x05 \x01(\x08\x12#\n\x05speed\x18\x06 \x01(\x0b\x32\x14.robot.CarData.Speed\x12)\n\x08position\x18\x07 \x01(\x0b\x32\x17.robot.CarData.Position\x12/\n\x0borientation\x18\x08 \x01(\x0b\x32\x1a.robot.CarData.Orientation\x1a.\n\x05Speed\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0f\n\x07\x61ngular\x18\x03 \x01(\x02\x1a \n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x1a\x39\n\x0bOrientation\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"\x9f\x01\n\nYoloResult\x12#\n\x04\x62oxs\x18\x01 \x03(\x0b\x32\x15.robot.YoloResult.Box\x12\x0c\n\x04time\x18\x02 \x01(\x0c\x1a^\n\x03\x42ox\x12\n\n\x02x1\x18\x01 \x01(\x02\x12\n\n\x02y1\x18\x02 \x01(\x02\x12\n\n\x02x2\x18\x03 \x01(\x02\x12\n\n\x02y2\x18\x04 \x01(\x02\x12\r\n\x05label\x18\x05 \x01(\t\x12\x0c\n\x04\x63onf\x18\x06 \x01(\x02\x12\n\n\x02id\x18\x07 \x01(\x05\"\x8c\x01\n\nFaceResult\x12\'\n\x04\x62oxs\x18\x01 \x03(\x0b\x32\x19.robot.FaceResult.FaceBox\x12\x0c\n\x04time\x18\x02 \x01(\x0c\x1aG\n\x07\x46\x61\x63\x65\x42ox\x12\n\n\x02x1\x18\x01 \x01(\x02\x12\n\n\x02y1\x18\x02 \x01(\x02\x12\n\n\x02x2\x18\x03 \x01(\x02\x12\n\n\x02y2\x18\x04 \x01(\x02\x12\x0c\n\x04name\x18\x05 \x01(\t\"\x9b\x01\n\x10YoloActionResult\x12/\n\x04\x62oxs\x18\x01 \x03(\x0b\x32!.robot.YoloActionResult.ActionBox\x12\x0c\n\x04time\x18\x02 \x01(\x0c\x1aH\n\tActionBox\x12\n\n\x02x1\x18\x01 \x01(\x02\x12\n\n\x02y1\x18\x02 \x01(\x02\x12\n\n\x02x2\x18\x03 \x01(\x02\x12\n\n\x02y2\x18\x04 \x01(\x02\x12\x0b\n\x03\x63ls\x18\x05 \x01(\t\"\x17\n\x08Keyboard\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1c\n\nCarMessage\x12\x0e\n\x06\x63\x61rmsg\x18\x01 \x01(\t\"-\n\tImageData\x12\x0c\n\x04time\x18\x01 \x01(\x0c\x12\x12\n\nimage_data\x18\x02 \x01(\x0c\x32\xce\x02\n\x05Robot\x12,\n\nGetCarData\x12\x0c.robot.Empty\x1a\x0e.robot.CarData\"\x00\x12\x32\n\rGetYoloResult\x12\x0c.robot.Empty\x1a\x11.robot.YoloResult\"\x00\x12\x32\n\rGetFaceResult\x12\x0c.robot.Empty\x1a\x11.robot.FaceResult\"\x00\x12>\n\x13GetYoloActionResult\x12\x0c.robot.Empty\x1a\x17.robot.YoloActionResult\"\x00\x12\x38\n\x10SetTwistKeyboard\x12\x0f.robot.Keyboard\x1a\x11.robot.CarMessage\"\x00\x12\x35\n\x0fGetHeadCamImage\x12\x0c.robot.Empty\x1a\x10.robot.ImageData\"\x00\x30\x01\x62\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_CARDATA = DESCRIPTOR.message_types_by_name['CarData']
_CARDATA_SPEED = _CARDATA.nested_types_by_name['Speed']
_CARDATA_POSITION = _CARDATA.nested_types_by_name['Position']
_CARDATA_ORIENTATION = _CARDATA.nested_types_by_name['Orientation']
_YOLORESULT = DESCRIPTOR.message_types_by_name['YoloResult']
_YOLORESULT_BOX = _YOLORESULT.nested_types_by_name['Box']
_FACERESULT = DESCRIPTOR.message_types_by_name['FaceResult']
_FACERESULT_FACEBOX = _FACERESULT.nested_types_by_name['FaceBox']
_YOLOACTIONRESULT = DESCRIPTOR.message_types_by_name['YoloActionResult']
_YOLOACTIONRESULT_ACTIONBOX = _YOLOACTIONRESULT.nested_types_by_name['ActionBox']
_KEYBOARD = DESCRIPTOR.message_types_by_name['Keyboard']
_CARMESSAGE = DESCRIPTOR.message_types_by_name['CarMessage']
_IMAGEDATA = DESCRIPTOR.message_types_by_name['ImageData']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'robot_data_pb2'
  # @@protoc_insertion_point(class_scope:robot.Empty)
  })
_sym_db.RegisterMessage(Empty)

CarData = _reflection.GeneratedProtocolMessageType('CarData', (_message.Message,), {

  'Speed' : _reflection.GeneratedProtocolMessageType('Speed', (_message.Message,), {
    'DESCRIPTOR' : _CARDATA_SPEED,
    '__module__' : 'robot_data_pb2'
    # @@protoc_insertion_point(class_scope:robot.CarData.Speed)
    })
  ,

  'Position' : _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
    'DESCRIPTOR' : _CARDATA_POSITION,
    '__module__' : 'robot_data_pb2'
    # @@protoc_insertion_point(class_scope:robot.CarData.Position)
    })
  ,

  'Orientation' : _reflection.GeneratedProtocolMessageType('Orientation', (_message.Message,), {
    'DESCRIPTOR' : _CARDATA_ORIENTATION,
    '__module__' : 'robot_data_pb2'
    # @@protoc_insertion_point(class_scope:robot.CarData.Orientation)
    })
  ,
  'DESCRIPTOR' : _CARDATA,
  '__module__' : 'robot_data_pb2'
  # @@protoc_insertion_point(class_scope:robot.CarData)
  })
_sym_db.RegisterMessage(CarData)
_sym_db.RegisterMessage(CarData.Speed)
_sym_db.RegisterMessage(CarData.Position)
_sym_db.RegisterMessage(CarData.Orientation)

YoloResult = _reflection.GeneratedProtocolMessageType('YoloResult', (_message.Message,), {

  'Box' : _reflection.GeneratedProtocolMessageType('Box', (_message.Message,), {
    'DESCRIPTOR' : _YOLORESULT_BOX,
    '__module__' : 'robot_data_pb2'
    # @@protoc_insertion_point(class_scope:robot.YoloResult.Box)
    })
  ,
  'DESCRIPTOR' : _YOLORESULT,
  '__module__' : 'robot_data_pb2'
  # @@protoc_insertion_point(class_scope:robot.YoloResult)
  })
_sym_db.RegisterMessage(YoloResult)
_sym_db.RegisterMessage(YoloResult.Box)

FaceResult = _reflection.GeneratedProtocolMessageType('FaceResult', (_message.Message,), {

  'FaceBox' : _reflection.GeneratedProtocolMessageType('FaceBox', (_message.Message,), {
    'DESCRIPTOR' : _FACERESULT_FACEBOX,
    '__module__' : 'robot_data_pb2'
    # @@protoc_insertion_point(class_scope:robot.FaceResult.FaceBox)
    })
  ,
  'DESCRIPTOR' : _FACERESULT,
  '__module__' : 'robot_data_pb2'
  # @@protoc_insertion_point(class_scope:robot.FaceResult)
  })
_sym_db.RegisterMessage(FaceResult)
_sym_db.RegisterMessage(FaceResult.FaceBox)

YoloActionResult = _reflection.GeneratedProtocolMessageType('YoloActionResult', (_message.Message,), {

  'ActionBox' : _reflection.GeneratedProtocolMessageType('ActionBox', (_message.Message,), {
    'DESCRIPTOR' : _YOLOACTIONRESULT_ACTIONBOX,
    '__module__' : 'robot_data_pb2'
    # @@protoc_insertion_point(class_scope:robot.YoloActionResult.ActionBox)
    })
  ,
  'DESCRIPTOR' : _YOLOACTIONRESULT,
  '__module__' : 'robot_data_pb2'
  # @@protoc_insertion_point(class_scope:robot.YoloActionResult)
  })
_sym_db.RegisterMessage(YoloActionResult)
_sym_db.RegisterMessage(YoloActionResult.ActionBox)

Keyboard = _reflection.GeneratedProtocolMessageType('Keyboard', (_message.Message,), {
  'DESCRIPTOR' : _KEYBOARD,
  '__module__' : 'robot_data_pb2'
  # @@protoc_insertion_point(class_scope:robot.Keyboard)
  })
_sym_db.RegisterMessage(Keyboard)

CarMessage = _reflection.GeneratedProtocolMessageType('CarMessage', (_message.Message,), {
  'DESCRIPTOR' : _CARMESSAGE,
  '__module__' : 'robot_data_pb2'
  # @@protoc_insertion_point(class_scope:robot.CarMessage)
  })
_sym_db.RegisterMessage(CarMessage)

ImageData = _reflection.GeneratedProtocolMessageType('ImageData', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDATA,
  '__module__' : 'robot_data_pb2'
  # @@protoc_insertion_point(class_scope:robot.ImageData)
  })
_sym_db.RegisterMessage(ImageData)

_ROBOT = DESCRIPTOR.services_by_name['Robot']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=27
  _EMPTY._serialized_end=34
  _CARDATA._serialized_start=37
  _CARDATA._serialized_end=421
  _CARDATA_SPEED._serialized_start=282
  _CARDATA_SPEED._serialized_end=328
  _CARDATA_POSITION._serialized_start=330
  _CARDATA_POSITION._serialized_end=362
  _CARDATA_ORIENTATION._serialized_start=364
  _CARDATA_ORIENTATION._serialized_end=421
  _YOLORESULT._serialized_start=424
  _YOLORESULT._serialized_end=583
  _YOLORESULT_BOX._serialized_start=489
  _YOLORESULT_BOX._serialized_end=583
  _FACERESULT._serialized_start=586
  _FACERESULT._serialized_end=726
  _FACERESULT_FACEBOX._serialized_start=655
  _FACERESULT_FACEBOX._serialized_end=726
  _YOLOACTIONRESULT._serialized_start=729
  _YOLOACTIONRESULT._serialized_end=884
  _YOLOACTIONRESULT_ACTIONBOX._serialized_start=812
  _YOLOACTIONRESULT_ACTIONBOX._serialized_end=884
  _KEYBOARD._serialized_start=886
  _KEYBOARD._serialized_end=909
  _CARMESSAGE._serialized_start=911
  _CARMESSAGE._serialized_end=939
  _IMAGEDATA._serialized_start=941
  _IMAGEDATA._serialized_end=986
  _ROBOT._serialized_start=989
  _ROBOT._serialized_end=1323
# @@protoc_insertion_point(module_scope)
