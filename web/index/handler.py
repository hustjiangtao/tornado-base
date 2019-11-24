# -*- coding: utf-8 -*-
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
