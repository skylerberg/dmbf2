from flask import Flask


app = Flask(__name__)

import dmbf2.views  # noqa
from dmbf2 import db  # noqa


__version__ = "0.0.1"
