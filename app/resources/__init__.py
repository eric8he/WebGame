from app import api, settings
from . import players

api.add_resource(players.UsersResource, '/users')
