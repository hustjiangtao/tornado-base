# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
index module unittest
"""


import tornado.escape
from tornado.testing import AsyncHTTPTestCase, gen_test

from web.run import Application


class TestConfig(AsyncHTTPTestCase):

    def get_app(self) -> Application:
        return Application()

    def test_index_page(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertIn('text/html', response.headers["Content-Type"])
        self.assertIn(b'Welcome', response.body)

    def test_index_json(self):
        response = self.fetch('/index.json')
        self.assertEqual(response.code, 200)
        self.assertIn('application/json', response.headers["Content-Type"])
        self.assertEqual(tornado.escape.json_decode(response.body)["code"], 0)
        self.assertIn('Welcome', tornado.escape.json_decode(response.body)["data"])
