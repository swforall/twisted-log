'''
Log server twistd application implementation
'''

from twisted.application import internet, service

from log_server import LoggerFactory
from settings_log_server import LOG_SERVER


application = service.Application("log_server")
logService = internet.TCPServer(LOG_SERVER[1], LoggerFactory())
logService.setServiceParent(application)