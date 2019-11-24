# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
config unittest
"""

import unittest

from web.settings import SETTINGS


class TestConfig(unittest.TestCase):

    def test_read(self):
        self.assertFalse(SETTINGS['debug'])
        self.assertTrue(SETTINGS['xsrf_cookies'])
