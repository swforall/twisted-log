'''
Configuration file for log server
'''

LOG_SERVER_FILE_NAME = 'log_server'

LOG_SERVER = ('localhost', 8080, 'log_server')

DB_NAME = 'log.db'
DB_TABLE = 'Log'
DB_FIELDS = ['time', 'hostname', 'pid', 'pname', 'exc_type', 'filename', 'line']

