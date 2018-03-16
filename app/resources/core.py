chain_id = 0;
player_id = 0;
class player_data_store:
	
	
	def __init__(self):
		players = dict()
		emails = []
		usernames = []
	
	def get(self,id):
		return self.players[id]
	
	def set(self,id, data):
		self.players[id]=data
		self.emails+=data.email
		self.usernames+=data.username
		
	def find_email(self,email):
		return email in self.emails
	
	def find_username(self,username):
		return username in self.usernames

class player:
	def __init__(self,email,username,password):
		self.cash=5000
		self.email=email
		self.username=username
		self.password=password
		self.created_chains=dict()
		self.others_chains=dict()
		self.players_queued=0
		self.player_queue = Queue()
		self.chains_queued=0
		self.chain_queue = Queue()

	def create_self_chain(self):
		if(ready_for_chain):
			k=[]
			for i in range(10):
				k += self.player_queue.get()
		self.created_chains[chain_id]=[n, 1]
		for i in range(10):
			k[i].queue_chain(2, self)
		chainId+=1
	
	def queue_player(self,new_player):
		self.players_queued+=1
		self.player_queue.put(new_player)
		
	def queue_chain(self,level,overlord_player):
		self.chains_queued+=1
		self.chain_queue.put([overlord_player,level])
	
	def continue_chain(self):
		if(ready_for_chain):
			k=[]
			for i in range(10):
				k += self.player_queue.get()
		self.others_chains[chain_id]= self.chain_queue.get()
		for i in range(10):
			k[i].queue_chain(self.others_chains[chain_id][1],self)
		chainId+=1
		
	def ready_for_chain(self):
		return self.players>=10
		
	def find_player(self):
		pass
		
