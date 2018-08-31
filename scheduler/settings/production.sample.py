"""Settings to override default settings in production."""
import os
import logging

#
# Override settings
#
DEBUG = False

HTTP_PORT = 1234
HTTP_ADDRESS = '12.34.56.78'

#
# Set logging level
#
logging.getLogger().setLevel(logging.DEBUG)

JOB_CLASS_PACKAGES = ['scheduler.job_types']

# MySQL Settings
DATABASE_CLASS = 'ndscheduler.core.datastore.providers.mysql.DatastoreMysql'

DATABASE_CONFIG_DICT = {
    'user': '',
    'password': '',
    'hostname': '',
    'port': 1234,
    'database': ''
}
