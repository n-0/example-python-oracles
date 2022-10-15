# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: persistor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import instrument_pb2 as instrument__pb2
import omen_pb2 as omen__pb2
import oracle_pb2 as oracle__pb2
import scenario_pb2 as scenario__pb2
import util_pb2 as util__pb2
import broker_pb2 as broker__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fpersistor.proto\x12\x0fworld.persistor\x1a\x10instrument.proto\x1a\nomen.proto\x1a\x0coracle.proto\x1a\x0escenario.proto\x1a\nutil.proto\x1a\x0c\x62roker.proto2\xea\x1f\n\tPersistor\x12O\n\x11\x63reate_instrument\x12\x1c.world.instrument.Instrument\x1a\x1c.world.instrument.Instrument\x12\x46\n\x0fread_instrument\x12\x15.world.util.QueryById\x1a\x1c.world.instrument.Instrument\x12O\n\x11update_instrument\x12\x1c.world.instrument.Instrument\x1a\x1c.world.instrument.Instrument\x12G\n\x11\x64\x65lete_instrument\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12Q\n\x10list_instruments\x12\x1b.world.util.QueryByIdFilter\x1a .world.instrument.InstrumentList\x12\x43\n\rcreate_oracle\x12\x18.world.oracle.OracleInfo\x1a\x18.world.oracle.OracleInfo\x12>\n\x0bread_oracle\x12\x15.world.util.QueryById\x1a\x18.world.oracle.OracleInfo\x12\x43\n\rupdate_oracle\x12\x18.world.oracle.OracleInfo\x1a\x18.world.oracle.OracleInfo\x12\x43\n\rdelete_oracle\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12I\n\x0clist_oracles\x12\x1b.world.util.QueryByIdFilter\x1a\x1c.world.oracle.OracleInfoList\x12\x45\n\x0f\x63reate_scenario\x12\x18.world.scenario.Scenario\x1a\x18.world.scenario.Scenario\x12@\n\rread_scenario\x12\x15.world.util.QueryById\x1a\x18.world.scenario.Scenario\x12\x45\n\x0fupdate_scenario\x12\x18.world.scenario.Scenario\x1a\x18.world.scenario.Scenario\x12\x45\n\x0f\x64\x65lete_scenario\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12K\n\x0elist_scenarios\x12\x1b.world.util.QueryByIdFilter\x1a\x1c.world.scenario.ScenarioList\x12j\n\x1c\x63reate_scenario_dependencies\x12$.world.scenario.ScenarioDependencies\x1a$.world.scenario.ScenarioDependencies\x12Y\n\x1aread_scenario_dependencies\x12\x15.world.util.QueryById\x1a$.world.scenario.ScenarioDependencies\x12j\n\x1cupdate_scenario_dependencies\x12$.world.scenario.ScenarioDependencies\x1a$.world.scenario.ScenarioDependencies\x12R\n\x1c\x64\x65lete_scenario_dependencies\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12\x63\n\x1alist_scenario_dependencies\x12\x1b.world.util.QueryByIdFilter\x1a(.world.scenario.ScenarioDependenciesList\x12U\n\x15\x63reate_scenario_state\x12\x1d.world.scenario.ScenarioState\x1a\x1d.world.scenario.ScenarioState\x12K\n\x13read_scenario_state\x12\x15.world.util.QueryById\x1a\x1d.world.scenario.ScenarioState\x12U\n\x15update_scenario_state\x12\x1d.world.scenario.ScenarioState\x1a\x1d.world.scenario.ScenarioState\x12K\n\x15\x64\x65lete_scenario_state\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12U\n\x13list_scenario_state\x12\x1b.world.util.QueryByIdFilter\x1a!.world.scenario.ScenarioStateList\x12Q\n\x17\x63reate_omen_series_info\x12\x1a.world.omen.OmenSeriesInfo\x1a\x1a.world.omen.OmenSeriesInfo\x12J\n\x15read_omen_series_info\x12\x15.world.util.QueryById\x1a\x1a.world.omen.OmenSeriesInfo\x12T\n\x15list_omen_series_info\x12\x1b.world.util.QueryByIdFilter\x1a\x1e.world.omen.OmenSeriesInfoList\x12Q\n\x17update_omen_series_info\x12\x1a.world.omen.OmenSeriesInfo\x1a\x1a.world.omen.OmenSeriesInfo\x12M\n\x17\x64\x65lete_omen_series_info\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12M\n\x10read_omen_series\x12\x1b.world.util.QueryByIdFilter\x1a\x1a.world.omen.OmenSeriesItem0\x01\x12O\n\x12insert_omen_series\x12\x1a.world.omen.OmenSeriesItem\x1a\x1b.world.util.RequestResponse(\x01\x12O\n\x12update_omen_series\x12\x1a.world.omen.OmenSeriesItem\x1a\x1b.world.util.RequestResponse(\x01\x12T\n\x17\x66ilter_omen_series_from\x12\x1a.world.omen.OmenSeriesItem\x1a\x1b.world.util.RequestResponse(\x01\x12\x43\n\rcreate_broker\x12\x18.world.broker.BrokerInfo\x1a\x18.world.broker.BrokerInfo\x12>\n\x0bread_broker\x12\x15.world.util.QueryById\x1a\x18.world.broker.BrokerInfo\x12\x43\n\rupdate_broker\x12\x18.world.broker.BrokerInfo\x1a\x18.world.broker.BrokerInfo\x12\x43\n\rdelete_broker\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12H\n\x0blist_broker\x12\x1b.world.util.QueryByIdFilter\x1a\x1c.world.broker.BrokerInfoList\x12>\n\x0e\x63reate_account\x12\x15.world.broker.Account\x1a\x15.world.broker.Account\x12<\n\x0cread_account\x12\x15.world.util.QueryById\x1a\x15.world.broker.Account\x12>\n\x0eupdate_account\x12\x15.world.broker.Account\x1a\x15.world.broker.Account\x12\x44\n\x0e\x64\x65lete_account\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12\x46\n\x0clist_account\x12\x1b.world.util.QueryByIdFilter\x1a\x19.world.broker.AccountList\x12\x38\n\x0c\x63reate_order\x12\x13.world.broker.Order\x1a\x13.world.broker.Order\x12\x38\n\nread_order\x12\x15.world.util.QueryById\x1a\x13.world.broker.Order\x12\x38\n\x0cupdate_order\x12\x13.world.broker.Order\x1a\x13.world.broker.Order\x12\x42\n\x0c\x64\x65lete_order\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12\x42\n\nlist_order\x12\x1b.world.util.QueryByIdFilter\x1a\x17.world.broker.OrderList\x12\x41\n\x0f\x63reate_position\x12\x16.world.broker.Position\x1a\x16.world.broker.Position\x12>\n\rread_position\x12\x15.world.util.QueryById\x1a\x16.world.broker.Position\x12\x41\n\x0fupdate_position\x12\x16.world.broker.Position\x1a\x16.world.broker.Position\x12\x45\n\x0f\x64\x65lete_position\x12\x15.world.util.QueryById\x1a\x1b.world.util.RequestResponse\x12H\n\rlist_position\x12\x1b.world.util.QueryByIdFilter\x1a\x1a.world.broker.PositionListb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'persistor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERSISTOR._serialized_start=123
  _PERSISTOR._serialized_end=4197
# @@protoc_insertion_point(module_scope)
