# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tick.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntick.proto\x12\nworld.tick\"G\n\nBidAskTick\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\x0b\n\x03\x61_v\x18\x02 \x01(\x01\x12\t\n\x01\x62\x18\x03 \x01(\x01\x12\x0b\n\x03\x62_v\x18\x04 \x01(\x01\x12\t\n\x01t\x18\x05 \x01(\x03\"M\n\tBasicTick\x12\t\n\x01o\x18\x01 \x01(\x01\x12\t\n\x01h\x18\x02 \x01(\x01\x12\t\n\x01\x63\x18\x03 \x01(\x01\x12\t\n\x01l\x18\x04 \x01(\x01\x12\t\n\x01v\x18\x05 \x01(\x03\x12\t\n\x01t\x18\x06 \x01(\x03\"\xc6\x01\n\x04Tick\x12\t\n\x01t\x18\x01 \x01(\x03\x12\"\n\x04kind\x18\x02 \x01(\x0e\x32\x14.world.tick.TickKind\x12\x14\n\x07minimal\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12)\n\x05\x62\x61sic\x18\x04 \x01(\x0b\x32\x15.world.tick.BasicTickH\x01\x88\x01\x01\x12,\n\x07\x62id_ask\x18\x05 \x01(\x0b\x32\x16.world.tick.BidAskTickH\x02\x88\x01\x01\x42\n\n\x08_minimalB\x08\n\x06_basicB\n\n\x08_bid_ask*.\n\x08TickKind\x12\x0b\n\x07Minimal\x10\x00\x12\n\n\x06\x42idAsk\x10\x01\x12\t\n\x05\x42\x61sic\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tick_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TICKKIND._serialized_start=379
  _TICKKIND._serialized_end=425
  _BIDASKTICK._serialized_start=26
  _BIDASKTICK._serialized_end=97
  _BASICTICK._serialized_start=99
  _BASICTICK._serialized_end=176
  _TICK._serialized_start=179
  _TICK._serialized_end=377
# @@protoc_insertion_point(module_scope)
