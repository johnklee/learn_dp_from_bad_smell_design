"""Logger utility."""

import coloredlogs
import logging


logging.basicConfig(level=logging.INFO)

def get_logger(obj, level = logging.DEBUG):
  logger = logging.getLogger(obj.__class__.__name__)
  logger.setLevel(level)
  coloredlogs.install(
      level='DEBUG',
      fmt='%(asctime)s %(name)s[%(levelname)s] %(message)s',
      logger=logger)
  return logger
