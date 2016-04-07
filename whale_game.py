import os, sys
import pygame
from pygame.locals import *
from whale import Whale

def load_image(filename):
	image = pygame.image.load(filename).convert()
	rect = image.get_rect()
	return image, rect
	
def run_game():
	pygame.init()
	
	size = width, height = 750, 500
	color = 210, 210, 210 
	o_speed = [1, 1]
	direction = False
	screen = pygame.display.set_mode(size)
	
	whale = Whale()
	octopus, oct_rect = load_image('octopus.gif')
	sprites = pygame.sprite.RenderPlain((whale))

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		
		oct_rect = oct_rect.move(o_speed)	
		
		if oct_rect.left < 0 or oct_rect.right > 750:
			o_speed[0] = -o_speed[0]
		
		if oct_rect.top < 0 or oct_rect.bottom > 500:
			o_speed[1] = -o_speed[1]

	
		screen.fill(color)
		sprites.update()
		sprites.draw(screen)
		screen.blit(octopus, oct_rect)
		pygame.display.update()
		pygame.time.delay(10)
run_game()
