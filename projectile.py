import pygame

class Projectile(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('whale.gif').convert()
		self.rect = self.image.get_rect()
		self.speed = [1, 1]

	def update(self):
		self.move()

	def move(self):
		if self.rect.top < 0 or self.rect.bottom > 500:
			self.speed[1] = -self.speed[1]
		
		if self.rect.right > 750 or self.rect.left < 0:
			self.speed[0] = -self.speed[0]
		
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos