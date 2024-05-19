# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from morai_msgs/ObjectStatusListExtended.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import morai_msgs.msg
import std_msgs.msg

class ObjectStatusListExtended(genpy.Message):
  _md5sum = "c74a5b5ee3ba424f5d334390beb3ffc3"
  _type = "morai_msgs/ObjectStatusListExtended"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

int32 num_of_npcs
int32 num_of_pedestrian
int32 num_of_obstacle

ObjectStatusExtended[] npc_list
ObjectStatusExtended[] pedestrian_list
ObjectStatusExtended[] obstacle_list
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: morai_msgs/ObjectStatusExtended
int32 unique_id
int32 type
string name
float64 heading

geometry_msgs/Vector3 velocity
geometry_msgs/Vector3 acceleration
geometry_msgs/Vector3 size
geometry_msgs/Vector3 position

geometry_msgs/Quaternion orientation
int32 turn_signal
string[] global_path_info
int32 lane_departure
float32 distance_left_lane
float32 distance_right_lane
float32 object_yaw_rate
================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','num_of_npcs','num_of_pedestrian','num_of_obstacle','npc_list','pedestrian_list','obstacle_list']
  _slot_types = ['std_msgs/Header','int32','int32','int32','morai_msgs/ObjectStatusExtended[]','morai_msgs/ObjectStatusExtended[]','morai_msgs/ObjectStatusExtended[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,num_of_npcs,num_of_pedestrian,num_of_obstacle,npc_list,pedestrian_list,obstacle_list

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjectStatusListExtended, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.num_of_npcs is None:
        self.num_of_npcs = 0
      if self.num_of_pedestrian is None:
        self.num_of_pedestrian = 0
      if self.num_of_obstacle is None:
        self.num_of_obstacle = 0
      if self.npc_list is None:
        self.npc_list = []
      if self.pedestrian_list is None:
        self.pedestrian_list = []
      if self.obstacle_list is None:
        self.obstacle_list = []
    else:
      self.header = std_msgs.msg.Header()
      self.num_of_npcs = 0
      self.num_of_pedestrian = 0
      self.num_of_obstacle = 0
      self.npc_list = []
      self.pedestrian_list = []
      self.obstacle_list = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3i().pack(_x.num_of_npcs, _x.num_of_pedestrian, _x.num_of_obstacle))
      length = len(self.npc_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.npc_list:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.unique_id, _x.type))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.heading
        buff.write(_get_struct_d().pack(_x))
        _v1 = val1.velocity
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v2 = val1.acceleration
        _x = _v2
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v3 = val1.size
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v4 = val1.position
        _x = _v4
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v5 = val1.orientation
        _x = _v5
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.turn_signal
        buff.write(_get_struct_i().pack(_x))
        length = len(val1.global_path_info)
        buff.write(_struct_I.pack(length))
        for val2 in val1.global_path_info:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        _x = val1
        buff.write(_get_struct_i3f().pack(_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate))
      length = len(self.pedestrian_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.pedestrian_list:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.unique_id, _x.type))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.heading
        buff.write(_get_struct_d().pack(_x))
        _v6 = val1.velocity
        _x = _v6
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v7 = val1.acceleration
        _x = _v7
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v8 = val1.size
        _x = _v8
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v9 = val1.position
        _x = _v9
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v10 = val1.orientation
        _x = _v10
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.turn_signal
        buff.write(_get_struct_i().pack(_x))
        length = len(val1.global_path_info)
        buff.write(_struct_I.pack(length))
        for val2 in val1.global_path_info:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        _x = val1
        buff.write(_get_struct_i3f().pack(_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate))
      length = len(self.obstacle_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacle_list:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.unique_id, _x.type))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.heading
        buff.write(_get_struct_d().pack(_x))
        _v11 = val1.velocity
        _x = _v11
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v12 = val1.acceleration
        _x = _v12
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v13 = val1.size
        _x = _v13
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v14 = val1.position
        _x = _v14
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v15 = val1.orientation
        _x = _v15
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.turn_signal
        buff.write(_get_struct_i().pack(_x))
        length = len(val1.global_path_info)
        buff.write(_struct_I.pack(length))
        for val2 in val1.global_path_info:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        _x = val1
        buff.write(_get_struct_i3f().pack(_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.npc_list is None:
        self.npc_list = None
      if self.pedestrian_list is None:
        self.pedestrian_list = None
      if self.obstacle_list is None:
        self.obstacle_list = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.num_of_npcs, _x.num_of_pedestrian, _x.num_of_obstacle,) = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.npc_list = []
      for i in range(0, length):
        val1 = morai_msgs.msg.ObjectStatusExtended()
        _x = val1
        start = end
        end += 8
        (_x.unique_id, _x.type,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 8
        (val1.heading,) = _get_struct_d().unpack(str[start:end])
        _v16 = val1.velocity
        _x = _v16
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v17 = val1.acceleration
        _x = _v17
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v18 = val1.size
        _x = _v18
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v19 = val1.position
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v20 = val1.orientation
        _x = _v20
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 4
        (val1.turn_signal,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.global_path_info = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.global_path_info.append(val2)
        _x = val1
        start = end
        end += 16
        (_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate,) = _get_struct_i3f().unpack(str[start:end])
        self.npc_list.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pedestrian_list = []
      for i in range(0, length):
        val1 = morai_msgs.msg.ObjectStatusExtended()
        _x = val1
        start = end
        end += 8
        (_x.unique_id, _x.type,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 8
        (val1.heading,) = _get_struct_d().unpack(str[start:end])
        _v21 = val1.velocity
        _x = _v21
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v22 = val1.acceleration
        _x = _v22
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v23 = val1.size
        _x = _v23
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v24 = val1.position
        _x = _v24
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v25 = val1.orientation
        _x = _v25
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 4
        (val1.turn_signal,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.global_path_info = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.global_path_info.append(val2)
        _x = val1
        start = end
        end += 16
        (_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate,) = _get_struct_i3f().unpack(str[start:end])
        self.pedestrian_list.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacle_list = []
      for i in range(0, length):
        val1 = morai_msgs.msg.ObjectStatusExtended()
        _x = val1
        start = end
        end += 8
        (_x.unique_id, _x.type,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 8
        (val1.heading,) = _get_struct_d().unpack(str[start:end])
        _v26 = val1.velocity
        _x = _v26
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v27 = val1.acceleration
        _x = _v27
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v28 = val1.size
        _x = _v28
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v29 = val1.position
        _x = _v29
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v30 = val1.orientation
        _x = _v30
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 4
        (val1.turn_signal,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.global_path_info = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.global_path_info.append(val2)
        _x = val1
        start = end
        end += 16
        (_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate,) = _get_struct_i3f().unpack(str[start:end])
        self.obstacle_list.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3i().pack(_x.num_of_npcs, _x.num_of_pedestrian, _x.num_of_obstacle))
      length = len(self.npc_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.npc_list:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.unique_id, _x.type))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.heading
        buff.write(_get_struct_d().pack(_x))
        _v31 = val1.velocity
        _x = _v31
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v32 = val1.acceleration
        _x = _v32
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v33 = val1.size
        _x = _v33
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v34 = val1.position
        _x = _v34
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v35 = val1.orientation
        _x = _v35
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.turn_signal
        buff.write(_get_struct_i().pack(_x))
        length = len(val1.global_path_info)
        buff.write(_struct_I.pack(length))
        for val2 in val1.global_path_info:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        _x = val1
        buff.write(_get_struct_i3f().pack(_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate))
      length = len(self.pedestrian_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.pedestrian_list:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.unique_id, _x.type))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.heading
        buff.write(_get_struct_d().pack(_x))
        _v36 = val1.velocity
        _x = _v36
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v37 = val1.acceleration
        _x = _v37
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v38 = val1.size
        _x = _v38
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v39 = val1.position
        _x = _v39
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v40 = val1.orientation
        _x = _v40
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.turn_signal
        buff.write(_get_struct_i().pack(_x))
        length = len(val1.global_path_info)
        buff.write(_struct_I.pack(length))
        for val2 in val1.global_path_info:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        _x = val1
        buff.write(_get_struct_i3f().pack(_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate))
      length = len(self.obstacle_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacle_list:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.unique_id, _x.type))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.heading
        buff.write(_get_struct_d().pack(_x))
        _v41 = val1.velocity
        _x = _v41
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v42 = val1.acceleration
        _x = _v42
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v43 = val1.size
        _x = _v43
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v44 = val1.position
        _x = _v44
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v45 = val1.orientation
        _x = _v45
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.turn_signal
        buff.write(_get_struct_i().pack(_x))
        length = len(val1.global_path_info)
        buff.write(_struct_I.pack(length))
        for val2 in val1.global_path_info:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        _x = val1
        buff.write(_get_struct_i3f().pack(_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.npc_list is None:
        self.npc_list = None
      if self.pedestrian_list is None:
        self.pedestrian_list = None
      if self.obstacle_list is None:
        self.obstacle_list = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.num_of_npcs, _x.num_of_pedestrian, _x.num_of_obstacle,) = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.npc_list = []
      for i in range(0, length):
        val1 = morai_msgs.msg.ObjectStatusExtended()
        _x = val1
        start = end
        end += 8
        (_x.unique_id, _x.type,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 8
        (val1.heading,) = _get_struct_d().unpack(str[start:end])
        _v46 = val1.velocity
        _x = _v46
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v47 = val1.acceleration
        _x = _v47
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v48 = val1.size
        _x = _v48
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v49 = val1.position
        _x = _v49
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v50 = val1.orientation
        _x = _v50
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 4
        (val1.turn_signal,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.global_path_info = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.global_path_info.append(val2)
        _x = val1
        start = end
        end += 16
        (_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate,) = _get_struct_i3f().unpack(str[start:end])
        self.npc_list.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pedestrian_list = []
      for i in range(0, length):
        val1 = morai_msgs.msg.ObjectStatusExtended()
        _x = val1
        start = end
        end += 8
        (_x.unique_id, _x.type,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 8
        (val1.heading,) = _get_struct_d().unpack(str[start:end])
        _v51 = val1.velocity
        _x = _v51
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v52 = val1.acceleration
        _x = _v52
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v53 = val1.size
        _x = _v53
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v54 = val1.position
        _x = _v54
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v55 = val1.orientation
        _x = _v55
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 4
        (val1.turn_signal,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.global_path_info = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.global_path_info.append(val2)
        _x = val1
        start = end
        end += 16
        (_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate,) = _get_struct_i3f().unpack(str[start:end])
        self.pedestrian_list.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacle_list = []
      for i in range(0, length):
        val1 = morai_msgs.msg.ObjectStatusExtended()
        _x = val1
        start = end
        end += 8
        (_x.unique_id, _x.type,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 8
        (val1.heading,) = _get_struct_d().unpack(str[start:end])
        _v56 = val1.velocity
        _x = _v56
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v57 = val1.acceleration
        _x = _v57
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v58 = val1.size
        _x = _v58
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v59 = val1.position
        _x = _v59
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v60 = val1.orientation
        _x = _v60
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 4
        (val1.turn_signal,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.global_path_info = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.global_path_info.append(val2)
        _x = val1
        start = end
        end += 16
        (_x.lane_departure, _x.distance_left_lane, _x.distance_right_lane, _x.object_yaw_rate,) = _get_struct_i3f().unpack(str[start:end])
        self.obstacle_list.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_3i = None
def _get_struct_3i():
    global _struct_3i
    if _struct_3i is None:
        _struct_3i = struct.Struct("<3i")
    return _struct_3i
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_i3f = None
def _get_struct_i3f():
    global _struct_i3f
    if _struct_i3f is None:
        _struct_i3f = struct.Struct("<i3f")
    return _struct_i3f