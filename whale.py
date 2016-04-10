import pygame

class Whale(pygame.sprite.DirtySprite):

	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
		self.whale = pygame.image.load('whale.gif').convert()
		self.image = self.whale
		self.rect = self.image.get_rect()
		self.spout_counter = 0
		self.rect.top, self.rect.right = 50, 700
		self.speed = [1, 1]
		self.facing_right = True
		self.state = 'still'
		self.spouting = False
		self.health = 100

		self.spout_0 = pygame.image.load('spout00.gif').convert()
		self.spout_1 = pygame.image.load('spout0.gif').convert()
		self.spout_2 = pygame.image.load('spout.gif').convert()

	def update(self):
		if self.state == 'still':
			pass
		elif self.state == 'moveup':
			self.moveup()
		elif self.state == 'movedown':
			self.movedown()
		elif self.state == 'moveleft':
			self.moveleft()
		elif self.state == 'moveright':
			self.moveright()
		
		if self.spouting:
			self.spout()
	
	def movedown(self):
		self.speed[0] = 0
		
		if self.rect.bottom > 500:
			self.speed[1] = 0
		else:
			self.speed[1] = 1
		
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos

	
	def moveup(self):
		self.speed[0] = 0
		
		if self.rect.top < 0:
			self.speed[1] = 0
		else:
			self.speed[1] = -1
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos

	def moveright(self):
		self.speed[1] = 0
		
		if not self.facing_right:
			self.image = pygame.transform.flip(self.image, True, False)
			self.facing_right = True
		
		if self.rect.right > 750: 
			self.speed[0] = 0
		else:
			self.speed[0] = 1
			
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos
	
	def moveleft(self):
		self.speed[1] = 0
		
		if self.facing_right:
			self.image = pygame.transform.flip(self.image, True, False)
			self.facing_right = False
		
		if self.rect.left < 0:
			self.speed[0] = 0 
			
		else:
			self.speed[0] = -1

		new_pos = self.rect.move(self.speed)
		self.rect = new_pos
	
	def spout(self):

		if self.spout_counter == 1:
			self.image = pygame.transform.flip(self.spout_0, not self.facing_right, False) 
			self.spout_counter += 1
		
		elif self.spout_counter == 25:
			self.image = pygame.transform.flip(self.spout_1, not self.facing_right, False)
			self.spout_counter += 1
		
		elif self.spout_counter == 50:
			self.image = pygame.transform.flip(self.spout_2, not self.facing_right, False) 
			self.spout_counter += 1
		
		elif self.spout_counter == 75:
			self.image = pygame.transform.flip(self.whale, not self.facing_right, False)
			self.spout_counter = 0
			self.spouting = False
		else:
			self.spout_counter += 1
	
		

