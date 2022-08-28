# -*- coding: utf-8 -*-
"""Create an application instance."""
from psycopg2cffi import compat

compat.register()

from flask.helpers import get_debug_flag

from conduit.app import create_app
from conduit.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

if __name__ == "__main__":
    # NB: for the server port, read an environmental variable called "SERVER_PORT", or use a default value
    # SERVER_PORT = os.environ.get("SERVER_PORT", "5000")
    # app.run(host="0.0.0.0", port=int(SERVER_PORT))
    app.run(host="0.0.0.0", port=5000)
