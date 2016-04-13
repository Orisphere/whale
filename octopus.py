from enemy import Enemy
import pygame
import random

class Octopus(Enemy):

	def __init__(self):
		Enemy.__init__(self)
		self.image = pygame.image.load('octopus.gif').convert()
		self.rect = self.image.get_rect()
		self.speed = [2, 1]
		self.counter = 0
		self.health = 100
		print(self.rect.center)
	def update(self):
		self.move()
		self.counter += 1
	
	def move(self):
		if self.counter == 50 or self.counter == 150:
			self.speed[1] = -1 #y-axis speed
			print(self.rect.center)	
		elif self.counter == 100 or self.counter == 200:
			self.speed[1] = 1 
		
			print(self.rect.center)	
		elif self.counter == 275:
			self.speed[0] = 0
			self.speed[1] = 2
			print(self.rect.center)	
		elif self.counter == 325:
			self.speed = [0, 0]
			self.shoot()
				
			print(self.rect.center)	
		elif self.counter == 345:
			self.speed[0] = -2

			print(self.rect.center)	
		elif self.counter == 482:
			self.speed = [0, 0]
			self.shoot()
			print(self.rect.center)
		elif self.counter == 512:
			self.speed[0] = -2

		elif self.counter == 650:
			self.speed[0] = 0
			print(self.rect.center)
		
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos

	def shoot(self):
		pass
