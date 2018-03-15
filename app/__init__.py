import flask_restful
from flask import Flask

from . import settings

app = Flask(__name__)
app.config.from_object(settings)

api = flask_restful.Api(app)

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

from . import resources  # noqa
