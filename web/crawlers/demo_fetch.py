# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

import logging
from tornado import gen

from .base import BaseFetch


class DemoFetch(BaseFetch):
    def __init__(self):
        super(DemoFetch, self).__init__()
        pass

    def run(self):
        logging.info('ok')
        pass


async def main_loop():
    while True:
        DemoFetch().run()
        logging.warning('test complete.')
        await gen.sleep(600)  # every 600s
