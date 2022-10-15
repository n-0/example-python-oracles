import json
import csv
from datetime import datetime
from concurrent import futures
import grpc
from grpc_generated.oracle_pb2_grpc import OracleServicer, add_OracleServicer_to_server
from grpc_generated.scenario_pb2 import ScenarioState
from grpc_generated.tick_pb2 import BasicTick, Tick
from grpc_generated.util_pb2 import RequestResponse
from grpc_generated.omen_pb2 import ScenarioOmenSeriesItem, Omen, OmenSmoke
from confluent_kafka import Producer
import socket
from . import helper

conf = {'bootstrap.servers': "localhost:9092", 'client.id': socket.gethostname()}

producer = Producer(conf)

class Oracler(OracleServicer):

    def update(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def state(self, request, context):
        """scenario_id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def initialize(self, request: ScenarioState, context):
        try:
            print("Oracle is initialized")
            print(f'Received request {request}')
            scenario_id = request.scenario_id
            params: create_scenario.Parameter = json.loads(request.state)
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
                            item = ScenarioOmenSeriesItem(scenario_id=scenario_id, omen=Omen(tick=Tick(b_tick=tick)))
                            print(f'created the following tick {item}')
                            message = item.SerializeToString()
                            print(f'serialized it to message {message}')
                            producer.produce(scenario_id, key=str(line_number), value=message)
                            print(f'produced the message into the kafka')
                        except Exception as inst:
                            print(f'Skipping unparseable row {row}')
                            print(type(inst))
                            print(inst.args)
                            print(inst)
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
        return RequestResponse(success=True)


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


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  add_OracleServicer_to_server(Oracler(), server)
  server.add_insecure_port('[::]:10012')
  server.start()
  server.wait_for_termination()
