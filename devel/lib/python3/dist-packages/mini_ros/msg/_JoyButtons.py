# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mini_ros/JoyButtons.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class JoyButtons(genpy.Message):
  _md5sum = "be1de48c3b52ec87587be0e78c2cb8cd"
  _type = "mini_ros/JoyButtons"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int8 updown
int8 leftright
int8 left_bump
int8 right_bump"""
  __slots__ = ['updown','leftright','left_bump','right_bump']
  _slot_types = ['int8','int8','int8','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       updown,leftright,left_bump,right_bump

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(JoyButtons, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.updown is None:
        self.updown = 0
      if self.leftright is None:
        self.leftright = 0
      if self.left_bump is None:
        self.left_bump = 0
      if self.right_bump is None:
        self.right_bump = 0
    else:
      self.updown = 0
      self.leftright = 0
      self.left_bump = 0
      self.right_bump = 0

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
      buff.write(_get_struct_4b().pack(_x.updown, _x.leftright, _x.left_bump, _x.right_bump))
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
      end = 0
      _x = self
      start = end
      end += 4
      (_x.updown, _x.leftright, _x.left_bump, _x.right_bump,) = _get_struct_4b().unpack(str[start:end])
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
      buff.write(_get_struct_4b().pack(_x.updown, _x.leftright, _x.left_bump, _x.right_bump))
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
      end = 0
      _x = self
      start = end
      end += 4
      (_x.updown, _x.leftright, _x.left_bump, _x.right_bump,) = _get_struct_4b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4b = None
def _get_struct_4b():
    global _struct_4b
    if _struct_4b is None:
        _struct_4b = struct.Struct("<4b")
    return _struct_4b
