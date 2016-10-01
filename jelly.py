
from enemy import Enemy
import pygame

class Jelly(Enemy):

	def __init__(self, startingpos=[0, 0]):
		Enemy.__init__(self)
		self.image = pygame.image.load('jelly.gif').convert()
		self.rect = self.image.get_rect()
		self.rect.left += startingpos[0]
		self.rect.top += startingpos[1]
		self.speed = [1, 1] 
		self.health = 100
	
	def update(self):
		self.move()
	
	def move(self):
		
		if self.rect.top < 0 or self.rect.bottom > 500:
			self.speed[1] = -self.speed[1]
		if self.rect.left < 0 or self.rect.right > 750:
			self.speed[0] = -self.speed[0]

		new_pos = self.rect.move(self.speed)
		self.rect = new_pos

	def shoot(self):
		pass
