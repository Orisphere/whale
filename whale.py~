import sys, pygame


def run_game():
	pygame.init()
	
	size = 750, 500
	white = 230, 230, 230 
	speed = [1, 1]
	direction = False
	screen = pygame.display.set_mode(size)
	whale = pygame.image.load('whale.gif').convert()
	whale_rect = whale.get_rect()
	spout00 = pygame.image.load('spout00.gif').convert()
	spout0 = pygame.image.load('spout0.gif').convert()
	spout = pygame.image.load('spout.gif').convert()


	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		whale_rect = whale_rect.move(speed)
		
		if whale_rect.left < 0 or whale_rect.right > 750:
			speed[0] = -speed[0]
			whale = pygame.transform.flip(whale, True, False)
			direction = not direction

		if whale_rect.top < 0: 
			speed[1] = -speed[1]
				
			screen.fill(white)
			screen.blit(pygame.transform.flip(spout00, direction, False), whale_rect)
			pygame.display.flip()
			pygame.time.delay(50)

			screen.fill(white)
			screen.blit(pygame.transform.flip(spout0, direction, False), whale_rect)
			pygame.display.flip()
			pygame.time.delay(50)

			screen.fill(white)
			screen.blit(pygame.transform.flip(spout, direction, False), whale_rect)
			pygame.display.flip()
			pygame.time.delay(800)
			
			screen.fill(white)
			screen.blit(whale, whale_rect)
			
		if whale_rect.bottom > 500:
			speed[1] = -speed[1]

		screen.fill(white)
		screen.blit(whale, whale_rect)
		pygame.display.flip()
		pygame.time.delay(10)
run_game()
