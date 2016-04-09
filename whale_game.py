import os, sys
import pygame
from pygame.locals import *
from whale import Whale
from octopus import Octopus
from projectile import Projectile
	
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
			
			elif event.type == KEYDOWN:
				if event.key == K_UP or event.key == K_w:
					whale.state = 'moveup'
				if event.key == K_DOWN or event.key == K_s:
					whale.state = 'movedown'
				if event.key == K_LEFT or event.key == K_a:
					whale.state = 'moveleft'
				if event.key == K_RIGHT or event.key == K_d:
					whale.state = 'moveright'

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
				if whale.facing_right:
					launch_location = whale.rect.right
				else:
					launch_location = whale.rect.left
				
				bullet = Projectile(whale.facing_right, launch_location, whale.rect.top+(whale.rect.height/2))
				bullet_sprite = pygame.sprite.RenderPlain(bullet)
				sprites.add(bullet_sprite)

	
		screen.fill(color)
		sprites.update()
		sprites.draw(screen)
		pygame.display.update()
		pygame.time.delay(10)


if __name__ == '__main__': run_game()
