# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""sql models"""


from sqlalchemy import Column
from sqlalchemy import VARCHAR

from ..base.model import BaseModel


class UserModel(BaseModel):
    """
    table user
    """

    __tablename__ = "auth_user"
    email = Column(VARCHAR(100), nullable=False, unique=True, server_default='', comment='用户邮箱')
    name = Column(VARCHAR(100), nullable=False, server_default='', comment='用户名称')
    hashed_password = Column(VARCHAR(100), nullable=False, server_default='', comment='用户密码hash')
    ip = Column(VARCHAR(45), nullable=False, server_default='', comment="ip地址，标准格式，最长格式化")
