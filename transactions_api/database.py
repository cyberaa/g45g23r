#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql;

def manage_connection(config):
    try:
        return True, pymysql.connect(**config)
    except Exception as error:
        #log
        return False, ''