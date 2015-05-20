from flask import Flask
from config import config as cfg

app = Flask(__name__)

from app.example import controllers

# initial log application
if cfg.DEBUG:
    from logging import Formatter
    import logging
    file_handler = logging.FileHandler(cfg.LOG_FILE)
    if cfg.LOG_LEVEL not in [0, 10, 20, 30, 40, 50]:
        file_handler.setLevel(0)
    else:
        file_handler.setLevel(cfg.LOG_LEVEL)
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(file_handler)


