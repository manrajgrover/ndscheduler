#!/bin/bash

(
    cd /home/ubuntu/code/scheduler && \
    NDSCHEDULER_SETTINGS_MODULE=scheduler.settings.production \
    /home/ubuntu/code/scheduler/venv/bin/python /home/ubuntu/code/scheduler/scheduler/scheduler.py
)
