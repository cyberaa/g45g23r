#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import aumbry
import os
import json
from config import Config
from utilities import mysql_config_from_env, logging_config_from_env, mapping_logging


# Create helper for schema decorator
# Create load config from file
# Create load env vars
def setup_logging(cfg):
    filename = cfg['filename']
    level = cfg['level']
    log_format = cfg['format']

    # Create log file if not existent otherwise die
    if not os.path.exists(filename):
        try:
            with open(filename, 'w'):
                pass
        except OSError as os_error:
            logging.warn(os_error)
            return False, os_error
        except Exception as error:
            return False, error

    # Setup logging
    try:
        root_logger = logging.getLogger()
        root_logger.setLevel(mapping_logging(level))

        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(logging.Formatter(log_format))
        root_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(log_format))
        root_logger.addHandler(console_handler)

        logging.debug('Logging has started...')
        return root_logger
    except OSError as os_error:
        logging.error(os_error)
        return False, os_error
    except KeyError as key_error:
        logging.error('No logging configuration found.')
        return False, key_error
    except Exception as any_error:
        logging.error(any_error)
        return False, any_error


# TODO Make config dynamic by searching for ymls on conf folder
# TODO Add load from env
def setup_config(filepath):
    return load_yaml_config(filepath)


def load_yaml_config(filepath):
    if os.path.exists(filepath):
        cfg = aumbry.load(
            aumbry.FILE,
            Config,
            {
                'CONFIG_FILE_PATH': filepath
            }
        )
        return cfg
    else:
        logging.warn('Configuration file not found at' + file)
        return False


def load_env_vars():
    logging.debug('Overriding set environment variables...')
    mysql_config_from_env(os.environ)
    logging_config_from_env(os.environ)


#TODO map status
def response_handler(resp, body, status):
    resp.append_header('Cache-Control', 'no-cache')
    resp.status = status
    resp.body = json.dumps(body)
    return resp
