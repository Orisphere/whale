import os, sys
import pygame
from pygame.locals import *
from game_state import *

def run_game():
	
	
	state = StartState() 
	
	while 1:
		for event in pygame.event.get():
			if event.type == STATECHANGE:
				try:
					whale = state.whale
					state = eval(event.new_state)(whale)
				except:
					state = eval(event.new_state)()
			
			else:
				state.handle_event(event)
		state.update()
		pygame.time.delay(10)


if __name__ == '__main__': run_game()
