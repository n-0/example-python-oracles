import grpc
import json
from oracles import Parameter, CSVMeta, ColumnMapping
from grpc_generated.persistor_pb2_grpc import PersistorStub
from grpc_generated.oracle_pb2 import OracleInfo, ConventionalOracleState
from grpc_generated.scenario_pb2 import Scenario
from grpc_generated.tick_pb2 import Frequency, Day


def connect_persistor():
    channel = grpc.insecure_channel('localhost:10000')
    stub = PersistorStub(channel)
    return stub

def create_oracle():
    stub = connect_persistor()
    stub.create_oracle(OracleInfo(id="", ticker=["parse_csv"], url="http://0.0.0.0:10012"))

def create_scenario(params: Parameter, ticker: list[str]):
    stub = connect_persistor()
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
        oracle= "parse_csv",
        scenario_series_id= "",
        input_ticker= [],
        state= state,
        cycle= frequency
    ))


def barchart_silver():
    #create_oracle()
    palim: Parameter = {
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
            }
        ]
    }

    create_scenario(palim, ["silver_barchart_csv"])

if __name__ == "__main__":
    barchart_silver()
