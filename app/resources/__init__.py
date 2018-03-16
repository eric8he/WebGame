from app import api, settings
from . import (
	players,
	#core,
	interface
)
#api.add_resource(players.UsersResource, '/users')

api.add_resource(interface.index_page, '/')
api.add_resource(interface.signup_page, '/signup/')
#api.add_resource(i, '/users')
