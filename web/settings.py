# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""settings for web server"""

import os

from tornado.options import define, options
from tornado.log import enable_pretty_logging

from dotenv import dotenv_values

# default app env, will override if exists .env file
APP_ENV = {
    "SECRET_KEY": "random-string",
    "db_host": "localhost",
    "db_port": "3306",
    "db_name": "demo",
    "db_user": "test",
    "db_password": "123123",
}
# load app env from .env file and override the default, not os environemt
APP_ENV.update(dotenv_values())

# options settings
define("port", default=8000, help="run on the given port", type=int)
define("debug", default=False, help="debug mode", type=bool)
options.parse_command_line()

# log settings
enable_pretty_logging()

# seetings for path
ROOT = os.path.dirname(os.path.abspath(__file__))

__BASE_PACKAGE__ = ""
STATIC_PATH = os.path.join(ROOT, __BASE_PACKAGE__, "static")
TEMPLATE_PATH = os.path.join(ROOT, __BASE_PACKAGE__, "templates")
SECRET_KEY = APP_ENV.get("SECRET_KEY")

SETTINGS = {
    "debug": options.debug,
    "autoreload": options.debug,
    "static_path": STATIC_PATH,
    "template_path": TEMPLATE_PATH,
    "cookie_secret": SECRET_KEY,
    "xsrf_cookies": True,
    # "login_url": '/auth/login',
}


# mysql + mysqlclient
# DATABASE_URL = 'mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'.format(**APP_ENV)
SETTINGS["db"] = "mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4".format(
    **APP_ENV
)
