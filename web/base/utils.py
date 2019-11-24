# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


import json
import logging
import traceback
import bcrypt
import tornado.ioloop
import tornado.escape

from datetime import datetime, date
from ipaddress import ip_address, AddressValueError


class DateTimeEncoder(json.JSONEncoder):
    """DateTime encoder"""

    def default(self, o):
        if isinstance(o, datetime):
            encoded_object = o.strftime("%Y-%m-%dT%H:%M:%SGMT+08:00")
        elif isinstance(o, date):
            encoded_object = o.strftime("%Y-%m-%dGMT+08:00")
        else:
            encoded_object = json.JSONEncoder.default(self, o)
        return encoded_object


class HttpUtil:
    """网络工具"""

    @staticmethod
    def get_formated_ip(ip):
        try:
            rel_ip = ip_address(ip).exploded
        except AddressValueError as e:
            logging.info(traceback.format_exc())
            rel_ip = ''
        return rel_ip

    @staticmethod
    def get_formated_ua(ua):
        try:
            rel_ua = ua[:200]
        except Exception as e:
            logging.info(traceback.format_exc())
            rel_ua = ''
        return rel_ua


class AuthUtil:
    """认证工具"""

    @staticmethod
    async def get_hashed_password(password: str) -> str:
        hashed_password = await tornado.ioloop.IOLoop.current().run_in_executor(
            None,
            bcrypt.hashpw,
            tornado.escape.utf8(password),
            bcrypt.gensalt(),
        )
        hashed_password = tornado.escape.to_unicode(hashed_password)
        return hashed_password

    @staticmethod
    async def check_hashed_password(password: str, hashed_password: str) -> bool:
        is_hashed_password = await tornado.ioloop.IOLoop.current().run_in_executor(
            None,
            bcrypt.checkpw,
            tornado.escape.utf8(password),
            tornado.escape.utf8(hashed_password),
        )
        return is_hashed_password
