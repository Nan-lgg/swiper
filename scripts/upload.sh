#!/bin/bash

LOCAL='./'
REMOTE='/opt/swiper'

USER='root'
HOST='35.194.171.19'

# 上传
rsync -crvP --exclude={.git,.venv,logs,__pycache__} $LOCAL $USER@$HOST:$REMOTE/

# 远程调用重启脚本
ssh $USER@$HOST "$REMOTE/scripts/restart.sh"
