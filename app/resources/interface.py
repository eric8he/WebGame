from flask import Flask, redirect
from flask_restful import Resource, reqparse
import msgpack as pack
import sys
from sty import fg, bg, ef, rs

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
		parser.add_argument('token',type=str, required=True)
		args = parser.parse_args()
		username = args.get('username')
		email = args.get("email")
		password = args.get('password')
		token = args.get('token')

		print(fg.blue+"[STATUS] "+fg.rs+"signup request, uname="+username+", email="+email+", passwd="+password, file=sys.stderr)
		print(fg.blue+"[STATUS] "+fg.rs+"user client token="+token, file=sys.stderr)
		if(args.get('password_conf')!=password or game.store.find_email(email) or game.store.find_username(username)):
			return redirect('../signup/', 301)
		game.store.set(core.player_id,game.player(email,username,game.encrypt_password(password)),token)
		print (fg.blue+"[STATUS] "+fg.rs+'Set up new player account.', file=sys.stderr)
		return redirect('../redirect/', 301)


class LogIn(Resource):
	def get(self):
		pass

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', type=str, required=True)
		parser.add_argument('password', type=str, required=True)
		parser.add_argument('token', type=str, required=True)
		args = parser.parse_args()
		username = args.get('username')
		password = args.get('password')
		trying_player_id = game.store.find_player_with_username(username)
		if (trying_player_id == -1 or game.store.get(trying_player_id).password != game.encrypt_password(password)):
			return redirect('../login/', 301)
		game.store.player_tokens[token]=game.store.player_tokens.pop(game.store.get(trying_player_id))
		return '{}, you are now logged in.'.format(username), 200

class GetData(Resource):
	def get(self,user_token):
		return pack.encode(game.store.get_from_token(user_token)), 200

	def post(self):
		pass

class Token(Resource):
	def get(self):
		pass

	def post(self, oldToken, newToken):
		game.store.player_tokens[newToken]=game.store.player_tokens.pop(oldToken)
