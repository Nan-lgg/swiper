#!/bin/bash

PROJ_DIR='/opt/swiper'
PID_FILE="$PROJ_DIR/logs/gunicorn.pid"

# 简单粗暴
# $PROJ_DIR/scripts/stop.sh
# $PROJ_DIR/scripts/start.sh

# 平滑重启
if [ -f $PID_FILE ];then
    kill -HUP $(cat $PID_FILE)
else
    echo '找不到 PID 文件'
fi
