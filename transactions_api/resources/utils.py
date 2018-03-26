## /usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon


class HealthResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('OK')
