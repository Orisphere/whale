import os
from enemy import Enemy
import pygame
from random import choice
from Images import *

class Crab(Enemy):

	def __init__(self, startingpos=[0, 0]):
		Enemy.__init__(self)
		image_path = os.path.join(os.path.realpath('.'), 'Images', 'crab.gif')
		self.image = pygame.image.load(image_path).convert()
		self.rect = self.image.get_rect()
		self.rect.left += startingpos[0]
		self.rect.top += startingpos[1]
		self.speed = [0, 2] 
		self.health = 100
		self.counter = 0

	def update(self):
		self.move()
		self.counter += 1
	
	def move(self):
		if self.rect.top < 0 or self.rect.bottom > 500:
			self.speed[1] = -self.speed[1]
		if self.rect.left < 0 or self.rect.right > 750:
			self.speed[0] = -self.speed[0]
		
		elif self.counter >= 150:
			speeds = [[0, 2], [0, -2], [0, 2], [0, -2], [0, 2], [0, -2], [2, 0], [-2, 0]]
			if self.rect.bottom > 500 or self.rect.top < 0:
				self.speed = choice(speeds[2:])
			elif self.rect.right > 750 or self.rect.left < 0:
				self.speed = choice(speeds[:2])
			else:
				self.speed = choice(speeds)
			self.counter = 0
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos
