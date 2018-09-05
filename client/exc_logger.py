'''
Log observer used to send real time log messages to a log server.
'''


import json
import os

from twisted.python.log import FileLogObserver
from twisted.internet import reactor, protocol
from twisted.python.logfile import DailyLogFile
from twisted.python import log

from settings_daemons import LOG_SERVER
from helpers import compose_msg

class LogClient(protocol.Protocol):
   ''' Log server client used for communication to
   the log server '''

   def __init__(self, message):
       self.message = message

   def connectionMade(self):
       self.transport.write(self.message)

   def dataReceived(self, data):
       log.msg("Server said:", data)
       self.transport.loseConnection()

class LogClientFactory(protocol.ClientFactory):
   ''' Factory to construct the protocol '''

   def __init__(self, message):
       self.message = message

   def buildProtocol(self, addr):
       return LogClient(self.message)

   def clientConnectionFailed(self, connector, reason):
       log.msg("Connection failed.")
       reactor.stop()

   def clientConnectionLost(self, connector, reason):
       log.msg("Connection lost.")
       reactor.stop()

def sendMessage(message):
    ''' Construct the protocol and send the message '''

    reactor.connectTCP(LOG_SERVER[0], LOG_SERVER[1], LogClientFactory(message))

class ExceptionLogger(FileLogObserver):
    ''' Logger object implementing the emit method '''

    def emit(self, eventDict):
        if eventDict['isError']:
            # this is executed only if the event is an error

            msg = compose_msg(eventDict)
            if msg:
                # msg is not empty only if the exception is
                # from the list of exceptions we are concerned about
                msg = bytes(json.dumps(msg), 'utf-8')
                sendMessage(msg)
        FileLogObserver.emit(self, eventDict)

def logger(filename):
    ''' Create the log file and logger objects and return the needed method '''

    logfile = DailyLogFile(filename, os.getcwd())
    return ExceptionLogger(logfile).emit