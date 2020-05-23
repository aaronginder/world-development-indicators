import logging
from logging.config import dictConfig
import yaml

with open("./config/logger.yaml", "r") as f:
    cfg = f.read()
    log_cfg = yaml.safe_load(cfg)

dictConfig(log_cfg)

logger = logging.getLogger('WDI')
