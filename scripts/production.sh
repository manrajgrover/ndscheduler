#!/bin/bash

(
    cd /home/ubuntu/code/ndscheduler && \
        NDSCHEDULER_SETTINGS_MODULE=scheduler.settings.production \
        /home/ubuntu/code/ndscheduler/venv/bin/python /home/ubuntu/code/ndscheduler/scheduler/scheduler.py
)
