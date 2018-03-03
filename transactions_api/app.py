## /usr/bin/env python3
# -*- coding: utf-8 -*-
from transactions_api.resources import utils
import falcon
import multiprocessing
import gunicorn.app.base
from gunicorn.six import iteritems
from gunicorn.workers.sync import SyncWorker


'''Transaction API constructor'''
class TransactionAPI(falcon.API):
    def __init__(self, *args, **kwargs):
        super(TransactionAPI, self).__init__(*args, **kwargs)

        self.add_route('/utils/health', utils.UtilsResource())


app = TransactionAPI()