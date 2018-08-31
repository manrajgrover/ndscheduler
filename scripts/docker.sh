#!/bin/sh

# Run scheduler server inside docker container
## TODO: Move environment variables to docker compose file
source /venv/bin/activate && \
	NDSCHEDULER_SETTINGS_MODULE=scheduler.settings.production \
	python /root/scheduler/scheduler.py
