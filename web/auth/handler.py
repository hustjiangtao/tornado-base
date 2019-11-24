# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""url handlers"""


from ..base.handler import BaseHandler
from ..base.error import FAILED, USER_NAME_OR_PASSWORD_WRONG
from .service import add_user, get_user_by_email, check_user_password


class RegisterHandler(BaseHandler):
    """register handler"""

    def post(self):
        # add new user
        ip = self.request.remote_ip
        uid = add_user(
            email=self.get_json_argument('email'),
            name=self.get_json_argument('name'),
            password=self.get_json_argument('password'),
            ip=ip,
        )

        if not uid:
            return self.render_json(error=FAILED)
        self.set_secure_cookie("user", str(uid))
        data = 'register success'
        return self.render_json(data=data)


class LoginHandler(BaseHandler):
    """login handler"""

    def post(self):
        user = get_user_by_email(email=self.get_json_argument('email'))
        if user and check_user_password(user=user, password=self.get_json_argument('password')):
            self.set_secure_cookie("user", str(user.id))
        else:
            return self.render_json(error=USER_NAME_OR_PASSWORD_WRONG)
        data = 'login success'
        return self.render_json(data=data)


class LogoutHandler(BaseHandler):
    """logout handler"""

    def get(self):
        self.clear_cookie("user")
        data = 'logout success'
        return self.render_json(data=data)
