# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""url routers for web server"""

from tornado.web import url

from . import handler

URL_HANDLERS = [
    url(r"/health", handler.IndexHandler, name="health_index"),
    url(r"/health_index.json", handler.IndexJsonHandler, name="health_index_json"),
]
