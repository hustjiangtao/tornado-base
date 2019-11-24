# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""handler services"""


from ..base.utils import HttpUtil, AuthUtil
from ..base.model import session_scope
from .model import UserModel


def get_user_count():
    result = UserModel.count()
    return result


def add_user(email: str, name: str, password, ip: str):
    result = UserModel.add(
        email=email,
        name=name,
        password=AuthUtil.get_hashed_password(password),
        ip=HttpUtil.get_formated_ip(ip),
    )
    return result


def get_user_by_email(email: str):
    with session_scope() as session:
        result = session.query(UserModel).filter_by(email=email).first()
    return result


def check_user_password(user: UserModel, password: str):
    result = AuthUtil.check_hashed_password(password, user.hashed_password)
    return result
