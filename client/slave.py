'''
Implementation of the daemons that raise exceptions.
Unhandled exceptions are raised by a command sent by a master daemon.
The master daemon controls what kind of error will occur.
Upon receiving the message, the slave daemon will raise the exception.
This file implements the slave daemon.
'''

from twisted.internet.protocol import Factory
from twisted.internet import protocol

from settings_daemons import EXCEPTIONS


class SlaveProtocol(protocol.Protocol):
    ''' Implement the protocol '''

    def __init__(self, factory):
        self.factory = factory
        self.msg = None

    def connectionMade(self):
        ''' Write a message to client on connection event '''

        self.broadcastMessage("Any wishes? Which exception to raise?")

    def connectionLost(self, reason):
        ''' Write a message to client on connection lost event '''

        self.broadcastMessage("Channel lost")

    def dataReceived(self, data):
        ''' Handle received data '''

        try:
            # expected data is a number, which specifies the type of exception
            data = int(data)
        except:
            # in case of invalid message, notify client and do nothing
            self.broadcastMessage("You sent: {}, No exception to raise".format(data.decode()))

        if data in EXCEPTIONS:
            # if number is not in EXCEPTIONS, do nothing
            self.broadcastMessage("Exception to raise - {}".format(EXCEPTIONS[data]))
            raise EXCEPTIONS[data]

    def broadcastMessage(self, message):
        ''' Serialize message and send it '''

        message = bytes(message, 'utf-8')
        self.transport.write(message)


class SlaveFactory(Factory):
    ''' Build the protocol '''

    def buildProtocol(self, addr):
        return SlaveProtocol(self)
