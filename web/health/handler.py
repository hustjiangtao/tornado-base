# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""url handlers"""


from ..base.handler import BaseHandler


class IndexHandler(BaseHandler):
    """index handler"""

    def get(self):
        return self.write('OK')


class IndexJsonHandler(BaseHandler):
    """index json handler"""

    def get(self):
        return self.render_json(data='OK')
