#! /usr/bin/env python3
# -*- coding: utf-8 -*-.
import sys
import logging
from middleware.logging import LoggingMiddleware
from app import TransactionAPI
from helpers import setup_logging, setup_config
from server import GunicornApp

CONFIG_FILE = './conf/config.yml'


config = setup_config(CONFIG_FILE)
log = setup_logging(config.logging)


def main():
    if config and log:
        api = TransactionAPI(config, middleware=[LoggingMiddleware(log)])
        app = GunicornApp(app=api, options=config.gunicorn)
        app.run()
    else:
        logging.error("Couldn't start app, config load failed at" + CONFIG_FILE)
        sys.exit(1)
