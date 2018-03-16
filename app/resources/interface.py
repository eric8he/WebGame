from flask import Flask
from flask_restful import Resource, reqparse
#import core
app = Flask(__name__)

#data_store=core.player_data_store()
#@app.route('/')


class index_page(Resource):
	def get(self):
		return self.html(),200

	def html(self):
		return '<!DOCTYPE html><html><head></head><body><a href="/signup/">Sign up</a><br /><a href="/login/">Log in</a></body></html>'

class signup_page(Resource):
	def get(self):
		return self.html(),200
		
	def html(self):
		return '<!DOCTYPE html><html><head></head><body><p>E-mail </p><input id="email"></input> <br /><p>Username </p><input id="username"></input> <br /><p>Password </p><input id="password"></input> <br /><p>Confirm Password </p><input id="password_conf"></input> <br /><p id="incorrect" style="color:red"></p><br /><button onclick="submit()">Sign Up</button><script>var submit=function(){var email = document.getElementById("email").value;var username = document.getElementById("username").value;var password = document.getElementById("password").value;if(document.getElementById("password_conf").value!=password){document.getElementById("incorrect").textContent="Passwords do not match!";return;}document.getElementById("incorrect").textContent="";window.location=window.location+"?email="email+"&username="+username+"&password="+password+"/";};</script></body></html>'
	

#@app.route('/signup/')

"""@app.route('/signup/<email>/<username>/<password>/')
def signup(email,username,password):
	if(data_store.find_email(email)):
		return '<!DOCTYPE html><html><head></head><body>That e-mail has already been used.<br /><a href="/signup/">Try again</a></body></html>'
	
	if(data_store.find_username(username)):
		return '<!DOCTYPE html><html><head></head><body>That username has already been used.<br /><a href="/signup/">Try again</a></body></html>'
	
	data_store.set(core.player_id,player(email,username,password))
	print ('Set up new player account.')"""
	