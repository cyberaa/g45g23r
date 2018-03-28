#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import falcon
from transactions_api.resources import utils


BASE_URI = '/api/v1'


'''Transaction API constructor'''
class TransactionAPI(falcon.API):
    def __init__(self, *args, **kwargs):
        super(TransactionAPI, self).__init__(*args, **kwargs)

        # Utils routes
        self.add_route(BASE_URI + '/utils/health', utils.HealthResource())
        self.add_route(BASE_URI + '/utils/meta', utils.MetaResource())

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker receives SIGHUPs/SIGINT/SIGKILL. """
        pass
