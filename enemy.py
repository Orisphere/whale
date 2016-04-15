import pygame

class Enemy(pygame.sprite.DirtySprite):

	def __init__(self):
		super().init()
		self.health = 100

	def update(self):
		pass

	def move(self):
		pass
	
