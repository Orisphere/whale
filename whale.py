import pygame

class Whale(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.whale = pygame.image.load('whale.gif').convert()
		self.image = self.whale
		self.rect = self.image.get_rect()
		self.spout_counter = 0
		self.rect.top, self.rect.right = 50, 700
		self.speed = [1, 1]
		self.direction = False

		self.spout_0 = pygame.image.load('spout00.gif').convert()
		self.spout_1 = pygame.image.load('spout0.gif').convert()
		self.spout_2 = pygame.image.load('spout.gif').convert()

	def update(self):
		if self.spout_counter == 0:
			self.move()
		else:
			if self.direction:
				self.spout_left()
			else:
				self.spout()

	def move(self):
		if self.rect.left < 0 or self.rect.right > 750:
			self.speed[0] = -self.speed[0]
			self.image = pygame.transform.flip(self.image, True, False)
			self.direction = not self.direction
			new_pos = self.rect.move(self.speed)

		if self.rect.bottom > 500:
			self.speed[1] = -self.speed[1]
			new_pos = self.rect.move(self.speed)

		if self.rect.top < 0:
			self.spout_counter += 1
			new_pos = self.rect
		else:
			new_pos = self.rect.move(self.speed)
		
		self.rect = new_pos

	def spout(self):

		if self.spout_counter == 1:
			self.image = self.spout_0
			self.speed = [0, 0]
			self.spout_counter += 1
		
		if self.spout_counter == 50:
			self.image = self.spout_1
			self.spout_counter += 1
		
		if self.spout_counter == 100:
			self.image = self.spout_2
			self.spout_counter += 1
		
		if self.spout_counter == 150:
			self.image = self.whale
			self.spout_counter = 0
			self.speed = [1, 1] #probably not right
			new_pos = self.rect.move(self.speed)
			self.rect = new_pos
		else:
			self.spout_counter += 1
	
	def spout_left(self):

		if self.spout_counter == 1:
			self.image = pygame.transform.flip(self.spout_0, True, False)
			self.speed = [0, 0]
			self.spout_counter += 1
		
		if self.spout_counter == 50:
			self.image = pygame.transform.flip(self.spout_1, True, False)
			self.spout_counter += 1
		
		if self.spout_counter == 100:
			self.image = pygame.transform.flip(self.spout_2, True, False)
			self.spout_counter += 1
		
		if self.spout_counter == 150:
			self.image = pygame.transform.flip(self.whale, True, False)
			self.spout_counter = 0
			self.speed = [-1, 1] #probably not right
			new_pos = self.rect.move(self.speed)
			self.rect = new_pos
		else:
			self.spout_counter += 1
	
