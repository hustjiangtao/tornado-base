# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""server for project
Usage:
    cd project/
    python -m webppx.run
"""

import logging
import traceback
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import options

from .settings import SETTINGS
from .url import URL_HANDLERS


class Application(tornado.web.Application):
    """initial application"""

    def __init__(self):
        tornado.web.Application.__init__(self, URL_HANDLERS, **SETTINGS)


def main():
    """main function to run server"""
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    try:
        logging.warning(f'server start...http://localhost:{options.port}')
        if options.debug:
            logging.warning('Debug mode')
        main()
    except KeyboardInterrupt:
        logging.warning("KeyboardInterrupt")
    else:
        logging.warning(traceback.format_exc())
