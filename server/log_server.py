'''
Logger server implementation
'''

import json

from twisted.internet import protocol

from very_simple_orm import DBEntry

class Logger(protocol.Protocol):
    ''' Logger class '''

    def dataReceived(self, data):
        ''' Implement only the data received handler method '''

        # deserialize received data and load it
        rec_obj = json.loads(data.decode())

        # create database entry and write it in the database
        dbobj = DBEntry(rec_obj)
        dbobj.write()

class LoggerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Logger()

