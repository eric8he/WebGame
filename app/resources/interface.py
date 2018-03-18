from flask import Flask, redirect
from flask_restful import Resource, reqparse

from . import core
app = Flask(__name__)

game = core.game()
	



class SignUp(Resource):

	def get(self):
		pass

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', type=str, required=True)
		parser.add_argument('email', type=str, required=True)
		parser.add_argument('password', type=str, required=True)
		parser.add_argument('password_conf', type=str, required=True)
		args = parser.parse_args()
		username = args.get('username')
		email = args.get("email")
		password = args.get('password')
		if(args.get('password_conf')!=password or game.store.find_email(email) or game.store.find_username(username)):
			return redirect('../signup/', 301)
		game.store.set(core.player_id,game.player(email,username,game.encrypt_password(password)))
		print ('Set up new player account.')
		return redirect('../redirect/', 301)
		
class LogIn(Resource):
	def get(self):
		pass

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', type=str, required=True)
		parser.add_argument('password', type=str, required=True)
		args = parser.parse_args()
		username = args.get('username')
		password = args.get('password')
		trying_player_id = game.store.find_player_with_username(username)
		if (trying_player_id == -1 or game.store.get(trying_player_id).password != game.encrypt_password(password)):
			return redirect('../login/', 301)
		return '{}, you are now logged in.'.format(username), 200
	