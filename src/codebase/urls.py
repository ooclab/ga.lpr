from tornado.web import url

from codebase.controllers import (
    default,
    npr
)


HANDLERS = [
    url(r"/",
        default.SpecHandler),

    url(r"/_health",
        default.HealthHandler),

    # NPR

    url(r"/npr",
        npr.NPRHandler),

]
