import pygame

import projectile

class Whale(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.whale = pygame.image.load('whale.gif').convert()
		self.image = self.whale
		self.rect = self.image.get_rect()
		self.spout_counter = 0
		self.rect.top, self.rect.right = 50, 700
		#self.speed = [1, 1]
		self.facing_right = True
		self.state = 'still'
		self.spouting = False

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
		#self.speed[0] = 0
		
		#if self.rect.bottom > 500:
			#self.speed[1] = 0
		#else:
			#self.speed[1] = 1
		if self.rect.bottom + 50 > 500:
			pass
		else:		
			new_pos = self.rect.move([0,50])
			self.rect = new_pos

	
	def moveup(self):
		if self.rect.top - 50 <= 0:
			pass
		else:		
			new_pos = self.rect.move([0,-50])
			self.rect = new_pos

	def moveright(self):
		if not self.facing_right:
			self.image = pygame.transform.flip(self.image, True, False)
			self.facing_right = True

		if self.rect.right + 50 > 750:
			pass
		else:		
			new_pos = self.rect.move([50,0])
			self.rect = new_pos
	
	def moveleft(self):
		if self.facing_right:
			self.image = pygame.transform.flip(self.image, True, False)
			self.facing_right = False

		if self.rect.left - 50 <= 0:
			pass
		else:		
			new_pos = self.rect.move([-50,0])
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
	
		

