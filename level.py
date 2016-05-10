from game_state import GameState
import random 

class Level(Object):

	def __init__(self):
		self.layout = [] #list of GameStates
		self.generate_layout()
		self.make_map()

	def generate_layout(self):
		size = random.random([6,7,8])
		direction = ['N', 'S', 'E', 'W']
		for __ in range(size):
			room = GameState() #Should be a specific room
			room.doors.append(random.random(direction)) #TODO: collision check on rooms

	def make_map(self):
		pass

