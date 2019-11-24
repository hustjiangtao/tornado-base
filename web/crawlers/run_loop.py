# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

from tornado import ioloop
from tornado.log import enable_pretty_logging

from .demo_fetch import main_loop as demo_loop


def main(loop):
    loop.spawn_callback(demo_loop)


if __name__ == '__main__':
    enable_pretty_logging()
    # ioloop.IOLoop.current().run_sync(main)
    # https://www.tornadoweb.org/en/stable/guide/coroutines.html#running-in-the-background
    # https://ia.jifangcheng.com/p/30
    main_loop = ioloop.IOLoop.current()
    # ioloop.IOLoop.current().spawn_callback(minute_loop)
    main(main_loop)
    ioloop.IOLoop.current().start()
