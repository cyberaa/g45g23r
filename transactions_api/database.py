#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import logging


def manage_connection(config):
    try:
        return True, pymysql.connect(**config)
    except Exception as error:
        logging.error(error)
        return False, error
