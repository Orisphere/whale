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
				if event.event_id == 'won':
					next_room = level.next_room()
					
					if next_room == 'Win':
						state = Win()
					else:
						state = Room(state.whale, enemies=level.enemies[next_room])

				elif event.event_id == 'lose':
					state = Lose()	
				
				elif event.event_id == 'start_over':
					level = Level()
					state = StartState()
			else:
				state.handle_event(event)
		state.update()
		pygame.time.delay(10)


if __name__ == '__main__': run_game()
