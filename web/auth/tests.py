# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
auth module unittest
"""


import tornado.escape
from tornado.testing import AsyncHTTPTestCase, gen_test

from web.run import Application


class TestConfig(AsyncHTTPTestCase):

    def get_app(self) -> Application:
        return Application()

    def test_auth_register(self):
        response = self.fetch('/auth/register')
        self.assertEqual(response.code, 405)

    def test_auth_login(self):
        response = self.fetch('/auth/login')
        self.assertEqual(response.code, 405)

    def test_auth_logout(self):
        response = self.fetch('/auth/logout')
        self.assertEqual(response.code, 200)
        self.assertEqual(tornado.escape.json_decode(response.body)["code"], 0)
