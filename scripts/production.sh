#!/bin/bash

# Install virtualenv
pip install virtualenv

# Install dependencies and run scheduler server
(
    cd .. && \
    rm -rf venv && \
    virtualenv venv && \
    pip install -r ./scheduler/requirements.txt && \
    pip install . && \
    NDSCHEDULER_SETTINGS_MODULE=scheduler.settings.production \
    python ./scheduler/scheduler.py
)
