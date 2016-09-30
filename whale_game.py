import os, sys
import pygame
from pygame.locals import *
from game_state import *

def run_game():
	
	
	state = StartState() 
	
	while 1:
		for event in pygame.event.get():
			if event.type == STATECHANGE:
				if event.new_state == "StartState":
					state = StartState()
				elif event.new_state == "Room_1":
					state = Room_1()
				elif event.new_state == "Room_2":
					whale = state.whale
					state = Room_2(whale)
				elif event.new_state == "Room_3":
					whale = state.whale
					state = Room_3(whale)
				elif event.new_state == "Win":
					state = Win()
				elif event.new_state == "Lose":
					state = Lose()
			else:
				state.handle_event(event)
		state.update()
		pygame.time.delay(10)


if __name__ == '__main__': run_game()
