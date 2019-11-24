# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


"""url routers for web server"""

from tornado.web import url

from .apps import app_url_modules

# from .index import handler as index_handler
# from .health import handler as health_handler
#
# URL_HANDLERS = [
#     url(r"/", index_handler.IndexHandler, name='index'),
#     url(r"/health", health_handler.HealthHandler, name='health'),
# ]

URL_HANDLERS = []
for x in app_url_modules:
    URL_HANDLERS.extend(x.URL_HANDLERS)
