#!/bin/bash

# Run scheduler server inside docker container
source /venv/bin/activate && \
	python /root/ndscheduler/scheduler/scheduler.py
