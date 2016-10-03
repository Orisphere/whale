import pygame
import projectile as projectile

class Drop(pygame.sprite.DirtySprite):
	def __init__(self):
		super().__init__()

	def update(self):
		pass #TODO: timer to time out drops

class DoryDrop(Drop):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('dory.gif').convert()
		self.rect = self.image.get_rect()
		self.type = "projectile"
		self.pickup = projectile.Dory()
