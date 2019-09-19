import tornado.web
from eva.conf import settings

from codebase.urls import HANDLERS
from codebase.utils.sqlalchemy import dbc


class Application(tornado.web.Application):
    def __init__(self):
        self.db_session = dbc.session

        tornado_settings = {
            "xsrf_cookies": False,
            "gzip": True,
            "debug": settings.DEBUG == "true",
            "secret_key": settings.SECRET_KEY,
        }

        tornado.web.Application.__init__(self, HANDLERS, **tornado_settings)


def make_app():
    return Application()
