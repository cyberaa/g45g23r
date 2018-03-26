import aumbry
from app import TransactionAPI
from gunicorn.app.base import BaseApplication
from gunicorn.workers.sync import SyncWorker
from config import Config



class ApiWorker(SyncWorker):
    def handle_quit(self, sig, frame):
        self.app.application.stop(sig)
        super(ApiWorker, self).handle_quit(sig, frame)

    def run(self):
        self.app.application.start()
        super(ApiWorker, self).run()


class GunicornApp(BaseApplication):
    """ Custom Gunicorn application

    This allows for us to load gunicorn settings from an external source
    """
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApp, self).__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)

        self.cfg.set('worker_class', 'transactions_api.__main__.ApiWorker')

    def load(self):
        return self.application


def main():
    #docopt(__doc__)

    cfg = aumbry.load(
        aumbry.FILE,
        Config,
        {
            'CONFIG_FILE_PATH': './conf/config.yml'
        }
    )

    api_app = TransactionAPI(cfg)
    gunicorn_app = GunicornApp(api_app, cfg.gunicorn)

    gunicorn_app.run()
