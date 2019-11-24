# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""url routers for web server"""

from tornado.web import url

from . import handler

URL_HANDLERS = [
    url(r"/", handler.IndexHandler, name="index"),
    url(r"/index.json", handler.IndexJsonHandler, name="index_json"),
]
