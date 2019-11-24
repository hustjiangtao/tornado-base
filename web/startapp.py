# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
start a new app under project
just like django: python manage.py startapp demo
usage:
    python -m web.startapp demo
    make startapp name=demo
"""

import os
import logging
import click


class Error(Exception):
    pass


init_text = '''# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
每个独立的模块应至少包含如下项目：
.
├── __init__.py
├── handler.py  路由处理（必选）
├── model.py  模型（必选，可为空）
├── schema.sql  数据库创建文件（可选）
├── service.py  业务逻辑（可选）
├── tests.py  单元测试（可选）
└── url.py  路由视图（必选）
新模块需要将模块名以字符串形式注册至 apps 中的 installed_apps
"""
'''

model_text = '''# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""sql models"""


from sqlalchemy import Column
from sqlalchemy import VARCHAR

from ..base.model import BaseModel


class IndexModel(BaseModel):
    """
    table index
    """

    __tablename__ = "{app_name}_index"
    ip = Column(VARCHAR(45), nullable=False, server_default='', comment="ip地址，标准格式，最长格式化")
    ua = Column(VARCHAR(200), comment="user agent，超出长度取前200位")
'''

schema_text = '''CREATE TABLE `{app_name}_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录ID',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `ip` varchar(45) NOT NULL DEFAULT '' COMMENT 'ip地址，标准格式，最长格式化',
  `ua` varchar(200) DEFAULT NULL COMMENT 'user agent，超出长度取前200位',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
'''

url_text = '''# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""url routers for web server"""

from tornado.web import url

from . import handler

URL_HANDLERS = [
    url(r"/{app_name}", handler.IndexHandler, name="{app_name}_index"),
    url(r"/{app_name}_index.json", handler.IndexJsonHandler, name="{app_name}_index_json"),
]
'''

handler_text = '''# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""url handlers"""


from datetime import datetime

from ..base.handler import BaseHandler
from .service import get_index_count, add_index


class IndexHandler(BaseHandler):
    """index handler"""

    def get(self):
        # get all index visitor count
        count = get_index_count()

        # add new index visitor
        ip = self.request.remote_ip
        ua = self.request.headers.get("User-Agent", "")
        add_index(ip=ip, ua=ua)

        data = f"Welcome! 现在时间是：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, 在您之前已经有 {count} 位访客啦。"
        return self.render("index.html", data=data)


class IndexJsonHandler(BaseHandler):
    """index json handler"""

    def get(self):
        # get all index visitor count
        count = get_index_count()

        # add new index visitor
        ip = self.request.remote_ip
        ua = self.request.headers.get("User-Agent", "")
        add_index(ip=ip, ua=ua)

        data = f"Welcome! 现在时间是：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, 在您之前已经有 {count} 位访客啦。"
        return self.render_json(data=data)
'''

service_text = '''# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""handler services"""


from ..base.utils import HttpUtil
from .model import IndexModel


def get_index_count():
    result = IndexModel.count()
    return result


def add_index(ip: str, ua: str):
    result = IndexModel.add(ip=HttpUtil.get_formated_ip(ip), ua=HttpUtil.get_formated_ua(ua))
    return result
'''

tests_text = '''# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
{app_name} module unittest
"""


import tornado.escape
from tornado.testing import AsyncHTTPTestCase, gen_test

from web.run import Application


class TestConfig(AsyncHTTPTestCase):

    def get_app(self) -> Application:
        return Application()

    def test_index_page(self):
        response = self.fetch('/{app_name}')
        self.assertEqual(response.code, 200)
        self.assertIn('text/html', response.headers["Content-Type"])
        self.assertIn(b'Welcome', response.body)

    def test_index_json(self):
        response = self.fetch('/{app_name}_index.json')
        self.assertEqual(response.code, 200)
        self.assertIn('application/json', response.headers["Content-Type"])
        self.assertEqual(tornado.escape.json_decode(response.body)["code"], 0)
        self.assertIn('Welcome', tornado.escape.json_decode(response.body)["data"])
'''


class StartApp:
    """start a new app"""

    current_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, app_name=None):
        self.app_name = app_name
        self.app_dir = os.path.join(self.current_dir, app_name)
        pass

    def write_app_file(self, name, content):
        with open(os.path.join(self.app_dir, name), 'w', encoding='utf-8') as f:
            f.write(content)

    def create_app_dir(self):
        try:
            os.mkdir(self.app_dir)
        except FileExistsError as e:
            raise Error(f"Dir {self.app_dir} already exists")
        except OSError as e:
            raise Error(e)
        pass

    def init_app(self):
        context = {
            "app_name": self.app_name,
        }
        self.write_app_file('__init__.py', init_text)
        self.write_app_file('model.py', model_text.format_map(context))
        self.write_app_file('schema.sql', schema_text.format_map(context))
        self.write_app_file('url.py', url_text.format_map(context))
        self.write_app_file('handler.py', handler_text)
        self.write_app_file('service.py', service_text)
        self.write_app_file('tests.py', tests_text.format_map(context))

    def run(self):
        self.create_app_dir()
        self.init_app()
        logging.warning(
            f'\nApp {self.app_name} created compolete!'
            f'\nThe app path is: {self.app_dir}'
            f'\nPlease do just as follow:'
            f'\n1. add app name: "{self.app_name}" to installed_apps in ./apps.py'
            f'\n2. to make migrations: `make migrations msg="add {self.app_name}"`'
            f'\n3. to apply the migrations: `make migrate`'
            f'\n4. to start the server: `make run` or `make dev`'
        )
        pass


@click.command()
@click.argument('app_name', nargs=1)
def main(app_name):
    starter = StartApp(app_name=app_name)
    starter.run()
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
