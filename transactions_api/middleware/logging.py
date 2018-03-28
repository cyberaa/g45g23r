#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class LoggingMiddleware():
    def __init__(self, log):
        self.log = log

    def process_response(self, req, resp, resource, req_succeeded):
        self.log.info('{0} {1} {2} {3} {4} {5}'.format(req.remote_addr, req.user_agent, req.method, req.relative_uri + req.query_string, resp.status[:3], req.scheme))
