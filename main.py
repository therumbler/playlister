import logging
import sys

from playlister.web import make_app


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = make_app()