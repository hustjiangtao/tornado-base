# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""sql models"""


from sqlalchemy import Column
from sqlalchemy import VARCHAR

from ..base.model import BaseModel


class IndexModel(BaseModel):
    """
    table index
    """

    __tablename__ = "index"
    ip = Column(VARCHAR(45), nullable=False, server_default='', comment="ip地址，标准格式，最长格式化")
    ua = Column(VARCHAR(200), comment="user agent，超出长度取前200位")
