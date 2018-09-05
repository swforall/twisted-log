#!/usr/bin/env bash

# create Logging database
sqlite3 log.db < init_db.sql

#TWISTD="/home/nayden/anaconda3/python /home/nayden/anaconda3/bin/twistd"
TWISTD=$(which twistd)

export PYTHONPATH=${PYTHONPATH}:$(pwd)

# start log server

# get log server name
# it is ugly, but works well to have the name in only one place
log_server_name=$(grep -oP "(?<=LOG_SERVER_FILE_NAME = ').+(?=')" settings_log_server.py)

${TWISTD} -y log_server.tac \
    --pidfile ${log_server_name}.pid --logfile ${log_server_name}.log &

echo 'Success, log server started!'