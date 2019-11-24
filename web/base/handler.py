# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


import json
import re

import tornado.web
import tornado.escape

from .utils import DateTimeEncoder
from .error import SUCCESS


class BaseHandler(tornado.web.RequestHandler):
    """Base class for other request handlers - all other handlers should
    base on this one.
    """

    def initialize(self):
        self.__set_header()

    def __set_header(self):
        self.set_header("Server", "MyServer")
        self.set_header("Cache-Control", "private")
        self.set_header('Version', 'v0.1')
        # self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.set_header('Content-Type', 'text/html; charset="utf-8"')
        # self.set_header('Access-Control-Allow-Methods', 'POST, PUT, GET, OPTIONS, DELETE')
        # self.set_header('Access-Control-Allow-Credentials', 'true')
        # self.set_header(
        #     'Access-Control-Allow-Headers',
        #     'Origin, X-Requested-With, Content-Type, Accept, client_id, uuid, Authorization'
        # )

        # # TODO test-only
        # # self.set_header('Access-Control-Allow-Origin', self.request.headers.get('Origin') or '*')
        # self.set_header('Access-Control-Allow-Origin', '*')

    def render_json(self, error=SUCCESS, data=None, **kwargs):
        """
        return json formatted data
        :param error: Error obj
        :param data: dict
        :return: bool
        """
        result = {
            "code": error.code,
            "message": error.message,
        }
        if data is not None:
            result["data"] = data
        result.update(kwargs)

        ua = self.request.headers.get('User-Agent', '')
        if re.match(r'.+\s+MSIE\s+.+', ua):
            content_type = 'text/html; charset=utf-8'
        else:
            content_type = 'application/json; charset=utf-8'
        self.set_header('Content-Type', content_type)

        self.write(json.dumps(result, ensure_ascii=False, cls=DateTimeEncoder))

    # def check_xsrf_cookie(self):
    #     """Ignore xsrf if ajax"""
    #     if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
    #         return

    def data_received(self, chunk):
        """Implement this method for tornado.web.RequestHandler"""
        pass

    def get_current_user(self):
        """determine the current user from, e.g., a cookie."""
        user_cookie = self.get_secure_cookie("user")
        if user_cookie:
            return json.loads(user_cookie)
        return None

    def get_json_argument(self, name, default=tornado.web._ARG_DEFAULT):
        """Get argument from application/json body"""
        content_type = self.request.headers.get("Content-Type", "")
        if content_type.startswith("application/json"):
            args = tornado.escape.json_decode(self.request.body)
            name = tornado.escape.to_unicode(name)
            if name in args:
                result = args[name]
            elif default is tornado.web._ARG_DEFAULT:
                raise tornado.web.MissingArgumentError(name)
            else:
                result = default

            return result
        return None
