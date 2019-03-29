#!/bin/bash

PROJ_DIR='/opt/swiper'
PID_FILE="$PROJ_DIR/logs/gunicorn.pid"

if [ -f $PID_FILE ]; then
    kill `cat $PROJ_DIR/logs/gunicorn.pid`
else
    echo 未找到 pid 文件
    exit 1
fi
