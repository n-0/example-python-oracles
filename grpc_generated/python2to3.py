import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path = os.path.join(path, 'grpc_generated') # package name where generated files are reside
file_path = f'{path}/*_pb2*.py*'
os.system(f'2to3 -wn -f import {file_path}')
