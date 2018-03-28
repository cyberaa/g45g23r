#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import pymysql

def mapping_logging(level):
    level = str.lower(level)

    if level == "debug":
        return logging.DEBUG
    elif level == "info":
        return logging.INFO
    elif level == "warning":
        return logging.WARNING
    elif level == "error":
        return logging.ERROR
    elif level == "critical":
        return logging.CRITICAL
    return logging.info


def mysql_config_from_env(env):
    return {
        'host': env.get('MYSQL_HOST', 'localhost'),
        'port': int(env.get('MYSQL_PORT', '3306')),
        'user': env.get('MYSQL_USER', 'root'),
        'pass': env.get('MYSQL_PASS', 'enumbra'),
        'database': env.get('MYSQL_DATABASE', 'enumbra'),
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }


def logging_config_from_env(env):
    return {
        'level': env.get('LOGGING_LEVEL', 'INFO'),
        'filename': env.get('LOGGING_FILENAME', './api.log')
    }