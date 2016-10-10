import os, sys
import pygame
from pygame.locals import *
from game_state import *
from level import Level
def run_game():
	
	
	state = StartState() 
	level = Level()
	while 1:
		for event in pygame.event.get():
			if event.type == STATECHANGE:
				room = level.next_room()
				try:
					whale = state.whale
					state = eval(room)(whale)
				except:
					state = eval(room)()
			
			else:
				state.handle_event(event)
		state.update()
		pygame.time.delay(10)


if __name__ == '__main__': run_game()
