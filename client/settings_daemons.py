'''
Configuration file for daemons
'''

EXCEPTIONS = {
    1: AssertionError,
    2: AttributeError,
    3: KeyError,
    4: ImportError,
    5: EOFError,
    6: FloatingPointError,
    7: GeneratorExit
    # this can be modified, so it contains more errors,
    # it also can be made to contain text, but more code
    # needs to be changed in this case
}

EXC_TIME = 10 # seconds
EXC_PROBABILITY = 1 # defined to 1, so that the master daemon always wants to raise exception

NUM_SLAVES = 5

SLAVES = [
    ('localhost', 8000, 'slave_daemon_0'),
    ('localhost', 8001, 'slave_daemon_1'),
    ('localhost', 8002, 'slave_daemon_2'),
    ('localhost', 8003, 'slave_daemon_3'),
    ('localhost', 8004, 'slave_daemon_4')
]

LOG_PARSER = {
    'time': 30, # seconds
    'types': ['AttributeError', 'EOFError', 'GeneratorExit'] # these are the types of errors we only check for
}

LOG_SERVER = ('192.168.56.102', 8080, 'log_server')


# currently needed only by the start bash scripts
SLAVE_DAEMONS_FILES_FORMAT = 'slave_daemon_'
MASTER_DAEMON_FILES_FORMAT = 'master'
