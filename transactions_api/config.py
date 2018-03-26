import aumbry
from aumbry import YamlConfig


class Config(aumbry.YamlConfig):
    __mapping__ = {
        'gunicorn': ['gunicorn', dict],
    }

    gunicorn = {}
