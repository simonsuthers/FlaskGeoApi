from flask import Flask
app = Flask(__name__)

import GeoApi.views
from .v1 import boundaries
