# -*- coding: utf-8 -*-
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
