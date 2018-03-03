import aumbry
from aumbry import YamlConfig

class AppConfig(aumbry.YamlConfig):
    __mapping__ = {
        'gunicorn': ['gunicorn', dict],
    }

    gunicorn = {}
