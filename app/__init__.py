import flask_restful
from flask import Flask, render_template

from . import settings

app = Flask(__name__)
app.config.from_object(settings)

api = flask_restful.Api(app)

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

from . import resources  # noqa
