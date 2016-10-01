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
		self.reverse = 1
	
	def update(self):
		self.move()
		self.counter += 1
	
	def move(self):
		mod = self.reverse
		
		if self.counter == 50 or self.counter == 150:
			self.speed[1] = -1 #y-axis speed
		
		elif self.counter == 100 or self.counter == 200:
			self.speed[1] = 1 
	#drop	
		elif self.counter == 275:
			self.speed[0] = 0
			self.speed[1] = 2
	#shoot	
		elif self.counter == 325:
			self.speed = [0, 0]
			self.shoot()
	#left			
		elif self.counter == 355:
			self.speed[0] = -2*mod
	#shoot
		elif self.counter == 492:
			self.speed = [0, 0]
			self.shoot()
	#left	
		elif self.counter == 522:
			self.speed[0] = -2*mod
	#shoot
		elif self.counter == 660:
			self.speed[0] = 0
	#drop	
		elif self.counter == 690:
			self.speed[1] = 2
	#bounce		
		elif self.counter == 785: 
			self.speed[0] = 2*mod
			self.speed[1] = -1 #Maybe error

		elif self.counter == 835 or self.counter == 935:
			self.speed[1] = 1 #y-axis speed
		
		elif self.counter == 885 or self.counter == 985:
			self.speed[1] = -1 
	#drop		
		elif self.counter == 1060:
			self.speed[0] = 0
			self.speed[1] = 2
	#rise	
		elif self.counter == 1100:
			self.speed[1] = -2
	#reverse	
		elif self.counter == 1285:
			self.speed[0] = -2*mod
			self.speed[1] =  1
			self.reverse = -self.reverse
			self.counter = 0

		new_pos = self.rect.move(self.speed)
		self.rect = new_pos

	def shoot(self):
		pass
