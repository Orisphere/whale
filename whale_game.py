import os, sys
import pygame
from pygame.locals import *
from whale import Whale
from octopus import Octopus
	
def run_game():
	pygame.init()
	
	size = width, height = 750, 500
	color = 210, 210, 210 
	screen = pygame.display.set_mode(size)
	
	whale = Whale()
	octopus = Octopus()
	sprites = pygame.sprite.RenderPlain((whale, octopus))

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		

	
		screen.fill(color)
		sprites.update()
		sprites.draw(screen)
		pygame.display.update()
		pygame.time.delay(10)
run_game()
