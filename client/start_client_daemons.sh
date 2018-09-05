#!/usr/bin/env bash

export PYTHONPATH=${PYTHONPATH}:$(pwd)
TWISTD=$(which twistd)

# start slave servers

# get number of slaves to raise exceptions
# it is ugly, but works well to have the number
num_slaves=$(($(grep -oP "(?<=NUM_SLAVES = )\d+" settings_daemons.py)-1))

# get slave name format
# it is ugly, but works well to have the name in only one place
slave_name=$(grep -oP "(?<=SLAVE_DAEMONS_FILES_FORMAT = ').+(?=')" settings_daemons.py)

for i in $(seq 0 ${num_slaves}); do
    ${TWISTD} -y slave_daemon_${i}.tac \
        --pidfile ${slave_name}${i}.pid &
done;


# start master server

# get master name format
master_name=$(grep -oP "(?<=MASTER_DAEMON_FILES_FORMAT = ').+(?=')" settings_daemons.py)

${TWISTD} -y master_daemon.tac \
    --pidfile ${master_name}.pid --logfile ${master_name}.log &

echo 'Success, clients started!'