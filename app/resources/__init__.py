from app import api, settings
from . import (
	players,
	interface,
	core
)


api.add_resource(players.UsersResource, '/users')
api.add_resource(interface.SignUp, '/signup')
api.add_resource(interface.LogIn, '/login')
api.add_resource(interface.GetData, '/getData')
api.add_resource(interface.Token, '/token')