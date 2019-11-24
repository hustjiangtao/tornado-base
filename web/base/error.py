# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
Common error code
all json response message should defined from here
"""


class Error(Exception):
    """请求返回信息"""

    def __init__(self, code: int, message: str):
        super().__init__(code, message)
        self.code = code
        self.message = message

    def __str__(self):
        return '{} {}'.format(self.code, self.message)


# status code
SUCCESS = Error(0, '成功')
FAILED = Error(1, '失败')
SYSTEM_ERROR = Error(2, '系统错误')
PARAMS_ERROR = Error(3, '参数错误')

# auth code
NOT_LOGINED = Error(4, '未登录')
ILLEGAL_REQUEST = Error(5, '非法请求')
NO_PERMISSION = Error(6, '无权操作')

# resource code
RESOURCE_NOT_FOUND = Error(7, '资源未找到')
RESOURCE_DUPLICATED = Error(8, '资源重复')

# user code
USER_INVISIBLE = Error(1000, '用户不可见')
USER_NAME_OR_PASSWORD_WRONG = Error(1001, '用户名或密码错误')
