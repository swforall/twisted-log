'''
This file was supposed to contain helper functions.
Only one was needed, so it maybe better if the function is in some of the other files,
but it was left this way anyway.
'''

import re
import socket
import psutil
from settings_daemons import LOG_PARSER

def compose_msg(source):
    ''' The message to be sent to the log server is composed here.
     If the exception is out of bounds, the dict will be empty.'''

    info_dict = {}

    exc = re.findall('[\w*]+Error(?=:)', source['log_text'])[0]
    if exc in LOG_PARSER['types']:
        info_dict['hostname'] = socket.gethostname()
        info_dict['exc_type'] = exc
        filename_and_line = re.findall(r'(?<= File ).*\d+(?=,)', source['log_text'])[-1]
        filename_and_line = filename_and_line.replace(',', '').replace('"', '').split()
        info_dict['filename'] = filename_and_line[0]
        info_dict['line'] = filename_and_line[-1]
        info_dict['time'] = source['time']
        info_dict['pid'] = psutil.Process().pid
        info_dict['pname'] = psutil.Process().exe()

    return info_dict