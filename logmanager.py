"""
Sets up the application logging. if it does not exist it creates a logs folder and a log file.
Log files are rotated at 1Mbyte intervals and the past 10 files are retained.
"""

import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from app_control import settings

# Ensure log directory exists
log_dir = os.path.dirname(settings['logfilepath'])
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getLogger(settings['logappname'])
"""
Usage:\n
**logger.info('message')** for info messages\n
**logger.warning('message')** for warnings\n
**logger.error('message')** for errors
"""

if settings['loglevel'].upper() == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

LogFile = RotatingFileHandler(settings['logfilepath'], maxBytes=1048576, backupCount=10)
formatter = logging.Formatter('%(asctime)s, %(name)s, %(levelname)s : %(message)s')
LogFile.setFormatter(formatter)
logger.addHandler(LogFile)
logger.info('Runnng Python %s on %s', sys.version, sys.platform)
logger.info('Logging level set to: %s', settings['loglevel'].upper())
