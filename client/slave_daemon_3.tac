'''
Slave daemon twistd application implementation
'''

from twisted.application import internet, service
from twisted.python.log import ILogObserver

from exc_logger import logger
from slave import SlaveFactory
from settings_daemons import SLAVES

application = service.Application(SLAVES[3][2])

# this is the line that needs to be added to this configuration, in order
# for the logger to work
application.setComponent(ILogObserver, logger('{}.log'.format(SLAVES[3][2])))

echoService = internet.TCPServer(SLAVES[3][1], SlaveFactory())
echoService.setServiceParent(application)