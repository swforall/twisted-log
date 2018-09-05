'''
Master daemon twistd application implementation.
This daemon will send messages to the slave daemons to
instruct them which exceptions to raise.
'''

from twisted.application import service
from twisted.application.internet import TimerService

from master_daemon import send_random_request
from settings_daemons import EXC_TIME


application = service.Application("master_daemon")
ts = TimerService(EXC_TIME, send_random_request)
ts.setServiceParent(application)