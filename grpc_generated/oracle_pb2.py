# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oracle.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import util_pb2 as util__pb2
import scenario_pb2 as scenario__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0coracle.proto\x12\x0cworld.oracle\x1a\nutil.proto\x1a\x0escenario.proto\"5\n\nOracleInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x03(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"8\n\x0eOracleInfoList\x12&\n\x04list\x18\x01 \x03(\x0b\x32\x18.world.oracle.OracleInfo2\xdc\x02\n\x06Oracle\x12\x44\n\x06update\x12\x1d.world.scenario.ScenarioState\x1a\x1b.world.util.RequestResponse\x12=\n\x05state\x12\x15.world.util.QueryById\x1a\x1d.world.scenario.ScenarioState\x12H\n\ninitialize\x12\x1d.world.scenario.ScenarioState\x1a\x1b.world.util.RequestResponse\x12H\n\rdefault_state\x12\x18.world.util.EmptyMessage\x1a\x1d.world.scenario.ScenarioState\x12\x39\n\x03\x65nd\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'oracle_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORACLEINFO._serialized_start=58
  _ORACLEINFO._serialized_end=111
  _ORACLEINFOLIST._serialized_start=113
  _ORACLEINFOLIST._serialized_end=169
  _ORACLE._serialized_start=172
  _ORACLE._serialized_end=520
# @@protoc_insertion_point(module_scope)
