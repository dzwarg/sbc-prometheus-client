#!/bin/bash
# /etc/init.d/p_client
### BEGIN INIT INFO
# Provides:          p_client
# Required-Start:    $remote_fs, $network
# Required-Stop:     $remote_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Prometheus Client
# Description:       Provide an endpoint for prometheus to gather data about this device.
### END INIT INFO

export WORKDIR=/usr/local/src/p_client
export VIRTUAL_ENV=${WORKDIR}/env
export PATH=${VIRTUAL_ENV}/bin:$PATH

cd $WORKDIR
./p_client.py
