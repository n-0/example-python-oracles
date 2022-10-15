from setuptools import setup

setup(
    name='python_oracles',
    version='0.1.0',
    description='Some helpful oracles for mr_world in python',
    author='Niklas Jona Lohmann',
    author_email='niklas.lohmann@tuhh.de',
    license='BSD 2-clause',
    packages=['oracles', 'grpc_generated'],
    install_requires=['grpcio-tools', 'grpcio', 'confluent_kafka'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)
