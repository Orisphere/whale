from enemy import Enemy
import pygame
import random

class Octopus(Enemy):

	def __init__(self):
		Enemy.__init__(self)
		self.image = pygame.image.load('octopus.gif').convert()
		self.rect = self.image.get_rect()
		self.speed = [1, 1]
		self.counter = 0
		self.health = 100

	def update(self):
		self.counter += 1
		self.move()

	def move(self):
		if self.rect.top < 0 or self.rect.bottom > 500:
			self.speed[1] = -self.speed[1]
			counter = 0
		if self.rect.right > 750 or self.rect.left < 0:
			self.speed[0] = -self.speed[0]
			counter = 0		
		if self.counter > 412:
			self.counter = 0
		
		elif self.counter%91 == 0:
			seq = [0, 1, 1, 2, -1, -1, -2]
			random.shuffle(seq)
			self.speed[0] = seq.pop()
			self.speed[1] = seq.pop()
		
		

		
		
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos

