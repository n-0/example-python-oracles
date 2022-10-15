import grpc
import json
from typing import TypedDict, Optional
from grpc_generated.persistor_pb2_grpc import PersistorStub
from grpc_generated.director_pb2_grpc import DirectorStub
from grpc_generated.oracle_pb2 import OracleInfo
from grpc_generated.scenario_pb2 import Scenario, ScenarioState
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


def example_parameter(path: str):
    return {
        'files': [
            {
             'path':"/home/no/mine/projects/finance/community-git/example-data/silver.csv",
             't_mapping': "%m/%d/%Y",
             'mapping': {
                't':0,
                'o':1,
                'h':2,
                'l':3,
                'c':4,
                'v':7
             }
        }]
    }

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

def create_scenario_state(stub, ticker: list[str], params):
    encoded_params = (json.dumps(params)).encode()
    stub.create_scenario_state(ScenarioState(ticker=ticker, state=encoded_params, scenario_id=""))


def create_scenario(stub, scenario_state_id, ticker: list[str], oracle_id: str):
    frequency = Frequency(every = 1, time_unit=Day)
    stub.create_scenario(Scenario(
        id= "",
        ticker= ticker,
        oracle= oracle_id,
        scenario_series_id= "",
        default_state=scenario_state_id,
    ))

