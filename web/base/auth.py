# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
tornado authenticated
"""

import functools
import urllib.parse as urlparse
from urllib.parse import urlencode

from tornado.web import HTTPError

from .error import NOT_LOGINED


def authenticated(method):
    """Decorate methods with this to require that the user be logged in.
    If the user is not logged in, they will be redirected to the configured
    `login url <RequestHandler.get_login_url>`.
    If you configure a login url with a query parameter, Tornado will
    assume you know what you're doing and use it as-is.  If not, it
    will add a `next` parameter so the login page knows where to send
    you once you're logged in.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            if self.request.method in ("GET", "HEAD"):
                url = self.get_login_url()
                if "?" not in url:
                    if urlparse.urlsplit(url).scheme:
                        # if login url is absolute, make next absolute too
                        next_url = self.request.full_url()
                    else:
                        next_url = self.request.uri
                    url += "?" + urlencode(dict(next=next_url))
                self.redirect(url)
                return
            raise HTTPError(403)
        return method(self, *args, **kwargs)
    return wrapper


def api_authenticated(method):
    """Decorate methods with this to require that the user be logged in.
    If the user is not logged in, they will raise http error 403.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            # raise HTTPError(403)
            return self.render_json(error=NOT_LOGINED)
        return method(self, *args, **kwargs)

    return wrapper
