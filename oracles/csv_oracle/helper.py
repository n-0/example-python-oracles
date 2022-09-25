import grpc
import json
from typing import TypedDict, Optional
from grpc_generated.persistor_pb2_grpc import PersistorStub
from grpc_generated.director_pb2_grpc import DirectorStub
from grpc_generated.oracle_pb2 import OracleInfo, ConventionalOracleState
from grpc_generated.scenario_pb2 import Scenario
from grpc_generated.tick_pb2 import Frequency, Day

class ColumnMapping(TypedDict):
    h: int
    l: int
    o: int
    c: int
    t: int
    v: int


class CSVMeta(TypedDict):
    path: str
    mapping: ColumnMapping
    t_mapping: Optional[str]

class Parameter(TypedDict):
    files: list[CSVMeta]



def connect_persistor():
    channel = grpc.insecure_channel('localhost:10000')
    stub = PersistorStub(channel)
    return stub

def connect_director():
    channel = grpc.insecure_channel('localhost:10001')
    stub = DirectorStub(channel)
    return stub

def create_oracle(stub, ticker: list[str]):
    stub.create_oracle(OracleInfo(id="", ticker=ticker, url="http://0.0.0.0:10012"))

def create_scenario(stub, params: Parameter, ticker: list[str], oracle_id: str):
    encoded_params = (json.dumps(params)).encode()
    state = ConventionalOracleState(
        scenario_id="",
        updates=[],
        parameter=encoded_params
    )
    frequency = Frequency(every = 1, time_unit=Day)
    stub.create_scenario(Scenario(
        id= "",
        ticker= ticker,
        oracle= oracle_id,
        scenario_series_id= "",
        input_ticker= [],
        state= state,
        cycle= frequency
    ))

