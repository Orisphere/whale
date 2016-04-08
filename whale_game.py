import os, sys
import pygame
from pygame.locals import *
from whale import Whale
from octopus import Octopus
	
def run_game():
	pygame.init()
	
	size = width, height = 750, 500
	tile_size = 50 #square tiles 50px x 50px
	color = 210, 210, 210 
	screen = pygame.display.set_mode(size)
	whale = Whale()
	octopus = Octopus()
	sprites = pygame.sprite.RenderPlain((whale, octopus))

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == KEYDOWN:
				if event.key == K_UP or event.key == K_w:
					whale.state = 'moveup'
				if event.key == K_DOWN or event.key == K_s:
					whale.state = 'movedown'
					pygame.time.delay(100)
				if event.key == K_LEFT or event.key == K_a:
					whale.state = 'moveleft'
					pygame.time.delay(100)
				if event.key == K_RIGHT or event.key == K_d:
					whale.state = 'moveright'
					pygame.time.delay(100)

			#only allow single-direction movement for the moment
			elif event.type == KEYUP:
				if (event.key == K_UP or event.key == K_w) and whale.state == 'moveup':
					whale.state = 'still'
				if (event.key == K_DOWN or event.key == K_s) and whale.state == 'movedown':
					whale.state = 'still'
				if (event.key == K_LEFT or event.key == K_a) and whale.state == 'moveleft':
					whale.state = 'still'
				if (event.key == K_RIGHT or event.key == K_d) and whale.state == 'moveright':
					whale.state = 'still'

			elif event.type == MOUSEBUTTONDOWN:
				whale.spouting = True

	
		screen.fill(color)
		for i in range(tile_size, width, tile_size):
			pygame.draw.lines(screen, (0,0,0), True, [(i, 0), (i, height)], 1)
		for i in range(tile_size, height, tile_size):
			pygame.draw.lines(screen, (0,0,0), True, [(0, i), (width, i)], 1)
		sprites.update()
		sprites.draw(screen)
		pygame.display.update()
		pygame.time.delay(10)


if __name__ == '__main__': run_game()
