import json
import csv
from datetime import datetime
from concurrent import futures
import grpc
from grpc_generated.oracle_pb2_grpc import OracleServicer, add_OracleServicer_to_server
from grpc_generated.oracle_pb2 import ConventionalOracleState
from grpc_generated.tick_pb2 import BasicTick, Tick
from grpc_generated.omen_pb2 import ScenarioOmenSeriesItem, Omen, OmenSmoke
from . import helper

class Oracler(OracleServicer):
    def update(self, request_iterator, context):
        yield Omen(smoke=OmenSmoke())

    def state(self, request, context):
        """scenario_id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def initialize(self, request: ConventionalOracleState, context):
        try:
            print("Oracle is initialized")
            print(f'Received request {request}')
            scenario_id = request.scenario_id
            params: create_scenario.Parameter = json.loads(request.parameter)
            ticks = list()
            print(f'with scenario_id {scenario_id}')
            print(f'and params {params}')
            for file in params['files']:
                print("Starting to iterate over files")
                with open(file['path']) as csvfile:
                    print("Was able to open file")
                    line_number = 0
                    reader = csv.reader(csvfile, delimiter=',')
                    print("Was able to read csv file")
                    for row in reader:
                        try:
                            if line_number == 0:
                                print("did continuation")
                                line_number += 1
                                continue
                            tick = BasicTick()
                            print("created basic tick")
                            for column in file['mapping'].keys():
                                if column == 't':
                                    if file['t_mapping'] == None:
                                        value = int(row[file['mapping'][column]])
                                    else:
                                        value = int(datetime.strptime(row[file['mapping'][column]], file['t_mapping']).timestamp()*1000)
                                elif column == 'v':
                                        value = int(row[file['mapping'][column]])
                                else:
                                    value = float(row[file['mapping'][column]])
                                tick.__setattr__(column, value)
                            line_number += 1
                            print(f'trying to produce {tick}')
                            yield ScenarioOmenSeriesItem(scenario_id=scenario_id, omen=Omen(tick=Tick(b_tick=tick)))
                        except Exception as inst:
                            print(f'Skipping unparseable row {row}')
                            print(type(inst))
                            print(inst.args)
                            print(inst)
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  add_OracleServicer_to_server(Oracler(), server)
  server.add_insecure_port('[::]:10012')
  server.start()
  server.wait_for_termination()
