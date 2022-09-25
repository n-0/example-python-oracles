# python oracles

Oracles (see [mr_world](https://github.com/n-0/mr_world)) written in python.
This repository contains 'utility oracles' to simplify daily operations e.g.
mining data (parsing csv files), among other things. It also serves as an
example/tutorial how to write and use oracles. Furthermore it will reveal
important structures outside of proto definitions. For example that an oracle
should provide a create_oracle, create_scenario helper functions to easily add
it to a mr_world configuration. It is by no means complete and isn't supposed to
be a metarepository for all python oracles.

## Tools for setup

Aside from the usual suspects (git, python, pip, protoc, grpc header files) one needs

```bash
pip install grpcio-tools
```

## Structure
The repository contains [mr_world_proto](https://github.com/n-0/mr_world_proto) as
a git submodule. The corresponding generated python files should be in `grpc_generated`, while
the actual oracle code is in `oracles`.
For code generation run

```bash
python -m grpc_tools.protoc -I=mr_world_proto/world/ --python_out=grpc_generated --grpc_python_out=grpc_generated mr_world_proto/world/*.proto
```

Unfortunately there is a known [issue](https://github.com/protocolbuffers/protobuf/issues/7061) 
in dealing with packages, so one has to run the following python code from the proto root (`grpc_generated`)

```python
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path = os.path.join(path, 'src') # package name where generated files are reside
file_path = f'{path}/*_pb2*.py*'
os.system(f'2to3 -wn -f import {file_path}')
```
for correct imports in the generated repository.

After installing the package via

```bash
python install .
```

it can be imported into other python files as

```python
import oracles
```

Read the [markdown](./oracles/README.md) files in `oracles` for details on the specific oracles.

**Author**: Niklas Jona Lohmann
