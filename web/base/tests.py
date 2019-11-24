# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
base utils unittest
"""


from tornado.testing import AsyncTestCase, gen_test

from web.base.utils import HttpUtil, AuthUtil


class TestConfig(AsyncTestCase):

    def test_http(self):
        self.assertEqual(HttpUtil.get_formated_ip('127.0.0.1'), '127.0.0.1')
        self.assertEqual(HttpUtil.get_formated_ua('123123'), '123123')

    @gen_test
    async def test_auth(self):
        password = '123123'
        self.assertTrue(await AuthUtil.check_hashed_password(password, await AuthUtil.get_hashed_password(password)))
