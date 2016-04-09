from enemy import Enemy
import pygame

class Octopus(Enemy):

	def __init__(self):
		Enemy.__init__(self)
		self.image = pygame.image.load('octopus.gif').convert()
		self.rect = self.image.get_rect()
		self.speed = [1, 1]
		self.counter = 0

	def update(self):
		self.counter += 1
		self.move()

	def move(self):
		if self.rect.top < 0 or self.rect.bottom > 500:
			self.speed[1] = -self.speed[1]
		if self.rect.right > 750 or self.rect.left < 0:
			self.speed[0] = -self.speed[0]
		
		if self.counter > 412:
			self.counter = 0
		
		elif self.counter == 51:
			self.speed[0] = self.speed[0]*2
		
		elif self.counter == 103:
			self.speed[1] = -self.speed[1]
		
		elif self.counter == 157:
			self.speed[0] = self.speed[0]/2 
		
		elif self.counter == 204:
			self.speed[1] = self.speed[1]*2
		
		elif self.counter == 247:
			self.speed[0] = -self.speed[0]	
		
		elif self.counter == 299:
			self.speed[1] = self.speed[1]/2

		elif self.counter == 351:
			self.speed[0] = -self.speed[0]
			self.speed[1] = -self.speed[1]
		
		
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos

