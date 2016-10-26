from game_state import GameState
import random 
from Enemies.octopus import Octopus
from Enemies.jelly import Jelly
from Enemies.hermit import Hermit
from Enemies.crab import Crab
from Enemies.sunfish import Sunfish

class Level:

	def __init__(self):
		self.generate_rooms()
		self.enemies = {'One': [Octopus()], 
				'Two': [Hermit(), Hermit(), Hermit(), Hermit(), Hermit()], 
				'Three': [Crab([250, 100]), Crab([500, 300]), Crab()],
				'Four': [Jelly()],
				'Five': [Sunfish()]}

	def next_room(self):
		return self.rooms.pop(0)

	
	def generate_rooms(self):	
		self.rooms = ['One', 'Two', 'Three', 'Four', 'Five']
		random.shuffle(self.rooms)
		self.rooms.append('Win')

	def make_map(self):
		pass


