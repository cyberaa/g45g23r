#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import falcon
from transactions_api.resources import utils


'''Transaction API constructor'''
class TransactionAPI(falcon.API):
    def __init__(self, *args, **kwargs):
        super(TransactionAPI, self).__init__(*args, **kwargs)

        self.add_route('/utils/health', utils.HealthResource())

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker starts shutting down. """
        pass