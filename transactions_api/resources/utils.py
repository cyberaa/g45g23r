#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import falcon
from ..helpers import response_handler as helpers_response_handler

class HealthResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""

        payload = [
            {
                "name": "mysql",
                "is_healthy": "",
            }
        ]
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('OK')


class MetaResource(object):
    def on_get(self, req, resp):
        payload = {
            "name": "Transaction API",
            "description": "API that manages transactions on Enumbra ICOs",
            "version": '0.1.0',
            "maintainer": "jjesusdei90@gmail.com"
        }

        helpers_response_handler(resp, payload, falcon.HTTP_200)
