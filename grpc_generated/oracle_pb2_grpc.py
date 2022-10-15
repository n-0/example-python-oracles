# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import scenario_pb2 as scenario__pb2
from . import util_pb2 as util__pb2


class OracleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.update = channel.unary_unary(
                '/world.oracle.Oracle/update',
                request_serializer=scenario__pb2.ScenarioState.SerializeToString,
                response_deserializer=util__pb2.RequestResponse.FromString,
                )
        self.state = channel.unary_unary(
                '/world.oracle.Oracle/state',
                request_serializer=util__pb2.QueryById.SerializeToString,
                response_deserializer=scenario__pb2.ScenarioState.FromString,
                )
        self.initialize = channel.unary_unary(
                '/world.oracle.Oracle/initialize',
                request_serializer=scenario__pb2.ScenarioState.SerializeToString,
                response_deserializer=util__pb2.RequestResponse.FromString,
                )
        self.default_state = channel.unary_unary(
                '/world.oracle.Oracle/default_state',
                request_serializer=util__pb2.EmptyMessage.SerializeToString,
                response_deserializer=scenario__pb2.ScenarioState.FromString,
                )
        self.end = channel.unary_unary(
                '/world.oracle.Oracle/end',
                request_serializer=util__pb2.QueryById.SerializeToString,
                response_deserializer=util__pb2.RequestResponse.FromString,
                )


class OracleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def update(self, request, context):
        """changing the state for a scenario while the oracle is running
        (some oracles wont support this)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def state(self, request, context):
        """the currently maintained state for the scenario_id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def initialize(self, request, context):
        """the initial state for the oracle specific to the scenario id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def default_state(self, request, context):
        """tried by persistor if no default state is provided 
        can be used to leave state creation to oracle code
        e.g. an the oracle accepts env vars and responds with
        a suitable encoded data (based on the vars) in bytes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def end(self, request, context):
        """the oracle doesnt need to produce any omens for the scenario anymore
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OracleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=scenario__pb2.ScenarioState.FromString,
                    response_serializer=util__pb2.RequestResponse.SerializeToString,
            ),
            'state': grpc.unary_unary_rpc_method_handler(
                    servicer.state,
                    request_deserializer=util__pb2.QueryById.FromString,
                    response_serializer=scenario__pb2.ScenarioState.SerializeToString,
            ),
            'initialize': grpc.unary_unary_rpc_method_handler(
                    servicer.initialize,
                    request_deserializer=scenario__pb2.ScenarioState.FromString,
                    response_serializer=util__pb2.RequestResponse.SerializeToString,
            ),
            'default_state': grpc.unary_unary_rpc_method_handler(
                    servicer.default_state,
                    request_deserializer=util__pb2.EmptyMessage.FromString,
                    response_serializer=scenario__pb2.ScenarioState.SerializeToString,
            ),
            'end': grpc.unary_unary_rpc_method_handler(
                    servicer.end,
                    request_deserializer=util__pb2.QueryById.FromString,
                    response_serializer=util__pb2.RequestResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'world.oracle.Oracle', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Oracle(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/world.oracle.Oracle/update',
            scenario__pb2.ScenarioState.SerializeToString,
            util__pb2.RequestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/world.oracle.Oracle/state',
            util__pb2.QueryById.SerializeToString,
            scenario__pb2.ScenarioState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def initialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/world.oracle.Oracle/initialize',
            scenario__pb2.ScenarioState.SerializeToString,
            util__pb2.RequestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def default_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/world.oracle.Oracle/default_state',
            util__pb2.EmptyMessage.SerializeToString,
            scenario__pb2.ScenarioState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def end(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/world.oracle.Oracle/end',
            util__pb2.QueryById.SerializeToString,
            util__pb2.RequestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
