import pygame

class Enemy(pygame.sprite.DirtySprite):

	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
		self.health = 100

	def update(self):
		pass

	def move(self):
		pass

