#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from gunicorn.app.base import BaseApplication
from gunicorn.workers.sync import SyncWorker


class ApiWorker(SyncWorker):
    def handle_quit(self, sig, frame):
        self.app.application.stop(sig)
        super(ApiWorker, self).handle_quit(sig, frame)

    def run(self):
        self.app.application.start()
        super(ApiWorker, self).run()


class GunicornApp(BaseApplication):
    """
        Get more Gunicorn control
    """
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApp, self).__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)

        self.cfg.set('worker_class', 'transactions_api.server.ApiWorker')

    def load(self):
        return self.application
