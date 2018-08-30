#!/bin/sh

# Run scheduler server inside docker container
source /venv/bin/activate && \
	NDSCHEDULER_SETTINGS_MODULE=scheduler.settings \
	python /root/scheduler/scheduler.py
