# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nutil.proto\x12\nworld.util\"\x1a\n\x0bGRPCAddress\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x0e\n\x0c\x45mptyMessage\"\"\n\x0fRequestResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x17\n\tQueryById\x12\n\n\x02id\x18\x01 \x01(\t\"=\n\x0fQueryByIdFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x06\x66ilter\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x42\t\n\x07_filter\"C\n\tFrequency\x12\r\n\x05\x65very\x18\x01 \x01(\x06\x12\'\n\ttime_unit\x18\x02 \x01(\x0e\x32\x14.world.util.TimeUnit\"%\n\tTimeRange\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x03\x12\n\n\x02to\x18\x02 \x01(\x03*a\n\x08TimeUnit\x12\x0f\n\x0bMillisecond\x10\x00\x12\n\n\x06Second\x10\x01\x12\n\n\x06Minute\x10\x02\x12\x08\n\x04Hour\x10\x03\x12\x07\n\x03\x44\x61y\x10\x04\x12\x08\n\x04Week\x10\x05\x12\x0f\n\x0bUnspecified\x10\x06\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TIMEUNIT._serialized_start=302
  _TIMEUNIT._serialized_end=399
  _GRPCADDRESS._serialized_start=26
  _GRPCADDRESS._serialized_end=52
  _EMPTYMESSAGE._serialized_start=54
  _EMPTYMESSAGE._serialized_end=68
  _REQUESTRESPONSE._serialized_start=70
  _REQUESTRESPONSE._serialized_end=104
  _QUERYBYID._serialized_start=106
  _QUERYBYID._serialized_end=129
  _QUERYBYIDFILTER._serialized_start=131
  _QUERYBYIDFILTER._serialized_end=192
  _FREQUENCY._serialized_start=194
  _FREQUENCY._serialized_end=261
  _TIMERANGE._serialized_start=263
  _TIMERANGE._serialized_end=300
# @@protoc_insertion_point(module_scope)
