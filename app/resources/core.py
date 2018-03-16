import queue, math, random
from . import util
chain_id = 0
player_id = 0
tick_state = 0

class game:
	
	class player_data_store:
		def __init__(self):
			self.players = dict()
			self.emails = []
			self.usernames = []
		
		def get(self,id):
			return self.players[id]
		
		def set(self,id, data):
			self.players[id]=data
			self.emails+=data.email
			self.usernames+=data.username

		def new_player(self,data):
			global player_id
			self.set(player_id,data)
			player_id += 1
			
		def find_email(self,email):
			return email in self.emails
		
		def find_username(self,username):
			return username in self.usernames
			
		def find_player_with_username(self,username):
			for key in self.players:
				if(self.players[key].username==username):
					return key
			return -1

	def encrypt_password(self,passwd):
		return passwd
	
	class player:
		def __init__(self,email,username,password):
			self.is_self = True
			self.tick_number = 0
			self.cash=5000
			self.email=email
			self.username=username
			self.password=password
			self.created_chains=dict()
			self.others_chains=dict()
			self.players_queued=0
			self.player_queue = queue.Queue()
			self.chains_queued=0
			self.chain_queue = queue.Queue()
			self.timer = util.RepeatedTimer(1000, self.tick)
			self.scouts = 0

		def create_self_chain(self):
			global chain_id
			if(self.ready_for_chain()):
				k=[]
				for i in range(10):
					k += self.player_queue.get()
			self.created_chains[chain_id]=[k, 1]
			for i in range(10):
				k[i].queue_chain(2, self)
			self.players_queued -= 10
			chain_id+=1
		
		def queue_player(self,new_player):
			self.players_queued += 1
			self.player_queue.put(new_player)
			
		def queue_chain(self,level,overlord_player):
			self.chains_queued += 1
			self.chain_queue.put([overlord_player,level])
		
		def continue_chain(self):
			global chain_id
			if(self.ready_for_chain()):
				k=[]
				for i in range(10):
					k += self.player_queue.get()
			self.others_chains[chain_id]= self.chain_queue.get()
			self.chains_queued -= 1
			for i in range(10):
				k[i].queue_chain(self.others_chains[chain_id][1],self)
			chain_id+=1
			
		def ready_for_chain(self):
			return self.players_queued>=10

		def tick(self):
			self.tick_number += 1
			for key in self.others_chains:
				self.cash += 10.0**(5-self.others_chains.get(key)[1])
			for key in self.created_chains:
				self.cash += 10.0**(5-self.others_chains.get(key)[1])
			
			if self.is_self:
				if self.tick_number%60 == 0:
					for i in range(0,self.scouts):
						self.queue_player(super.random_player())
					for i in range(0, math.ceil(self.scouts/10.0)):
						self.create_self_chain()
			
			if self.tick_number == 60:
				self.tick_number=0
		
		def buy_scout(self):
			if self.cash > 10000:
				self.cash -= 10000
				self.scouts += 1

		def set_scout_mode(self, is_self):
			self.is_self=is_self

	def __init__(self):
		self.store = self.player_data_store()
	
	def create_player(self,p):
		self.store.new_player(p)
	
	def random_player(self):
		return self.store.get(random.randint(0,player_id))