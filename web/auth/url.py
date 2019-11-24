# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""url routers for web server"""

from tornado.web import url

from . import handler

URL_HANDLERS = [
    url(r"/auth/register", handler.RegisterHandler, name="auth_register"),
    url(r"/auth/login", handler.LoginHandler, name="auth_login"),
    url(r"/auth/logout", handler.LogoutHandler, name="auth_logout"),
]
