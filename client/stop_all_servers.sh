#!/usr/bin/env bash
# Utility script for stopping all daemons

# send SIGTERM to all started twistd processes
kill -15 $(ps -ef | grep '[t]wistd -y' | awk '{print $2}')

if [ -z $(ps -ef | grep '[t]wistd -y' | awk '{print $2}') ]; then
    echo 'Successfully terminated all twistd services';
else
    echo 'There are left over services, please check'
fi

echo $(ps -ef | grep 'python')