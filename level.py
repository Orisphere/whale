from game_state import GameState
import random 

class Level:

	def __init__(self):
		self.generate_rooms()
		
	def next_room(self):
		return self.rooms.pop(0)

	
	def generate_rooms(self):	
		self.rooms = ['Room_1', 'Room_2', 'Room_3', 'Room_4', 'Room_5']
		random.shuffle(self.rooms)
		self.rooms.append('Win')
	
