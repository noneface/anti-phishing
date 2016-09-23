# coding: utf-8

# logging setting
#
# created by bsdr at 2016-09-22

import logging
import logging.handlers
import os

os.path.join(os.getcwd())
from config import LOG, DEBUG

log_file = os.path.join(os.getcwd(), "log", LOG.get("file"))
handler = logging.handlers.RotatingFileHandler(log_file, backupCount=5)
fmt = '[%(asctime)s] [%(levelname)s]:  %(filename)s:%(lineno)s -- %(funcName)s: %(module)s: %(message)s'    # log format

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('tst')
logger.addHandler(handler)


if DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.ERROR)



