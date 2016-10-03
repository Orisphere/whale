from game_state import GameState
import random 

class Level(Object):

	def __init__(self):
		self.rooms = ['StartState', 'Room_1', 'Room_2', 'Room_3', 'Room_4', 'Room_5','Win'] 
		

	def next_room(self):
		return self.rooms.pop(0)
