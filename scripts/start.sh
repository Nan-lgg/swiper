#!/bin/bash

PROJ_DIR='/opt/swiper'

cd $PROJ_DIR
source $PROJ_DIR/.venv/bin/activate
gunicorn -c $PROJ_DIR/swiper/gunicorn-config.py swiper.wsgi
deactivate
cd -
