#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from aumbry import YamlConfig


class Config(YamlConfig):
    __mapping__ = {
        'gunicorn': ['gunicorn', dict],
        'database': ['database', dict],
        'logging': ['logging', dict]
    }