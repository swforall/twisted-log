'''
Master daemon implementation.
This daemon will send messages to the slave daemons to
instruct them which exceptions to raise.
'''

from datetime import datetime
import os
import random

from twisted.internet import reactor, protocol
from twisted.python import log

from settings_daemons import EXCEPTIONS, EXC_PROBABILITY, SLAVES


class SlaveClient(protocol.Protocol):
   ''' Protocol to communicate with slave clients '''

   def __init__(self, message):
       self.message = message

   def connectionMade(self):
       ''' Send message to slave '''

       log.msg("Connection made.")
       self.transport.write(self.message)

   def dataReceived(self, data):
       ''' Log data received from slave '''

       log.msg("Slave said:", data)


class SlaveClientFactory(protocol.ClientFactory):
   ''' Factory to create protocols for communication with slave daemons '''

   def __init__(self, message):
       self.message = message

   def buildProtocol(self, addr):
       ''' Build the protocol '''

       log.msg("Build protocol.")
       return SlaveClient(self.message)

   def clientConnectionFailed(self, connector, reason):
       ''' Slave daemon connection failed '''

       log.msg("Connection failed.")

   def clientConnectionLost(self, connector, reason):
       ''' Slave daemon lost connection '''

       log.msg("Connection lost.")

def sendMessage(message, host):
    ''' Send the message '''

    log.msg('Host: ', host)
    reactor.connectTCP(host[0], host[1], SlaveClientFactory(message))


def send_random_request():
    ''' Choose whether to send a request for an exception randomly '''

    for h in SLAVES:
        # loop over all slave daemons
        log.msg("Current time: {}, pid: {}".format(datetime.now(), os.getpid()))
        if random.random() < EXC_PROBABILITY:
            e = random.randint(1, len(EXCEPTIONS))
            msg = bytes('{}'.format(e), 'utf-8')
            sendMessage(msg, h)