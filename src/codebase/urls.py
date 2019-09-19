from tornado.web import url

from codebase.controllers import (
    default,
    lpr
)


HANDLERS = [
    url(r"/",
        default.SpecHandler),

    url(r"/_health",
        default.HealthHandler),

    # NPR

    url(r"/lpr",
        lpr.LPRHandler),

]
