import pygame

class Projectile(pygame.sprite.Sprite):

	def __init__(self, is_facing_right, init_coord_x, init_coord_y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('whale.gif').convert()
		self.rect = self.image.get_rect()
		if is_facing_right:
			self.speed = [10, 0]
		else:
			self.speed = [-10, 0]
		self.start_coord_x = init_coord_x
		self.start_coord_y = init_coord_y

	def update(self):
		self.move()

	def move(self):
		if self.rect.top < 0 or self.rect.bottom > 500:
			self.speed[1] = -self.speed[1]
		
		if self.rect.right > 750 or self.rect.left < 0:
			self.speed[0] = -self.speed[0]
		
		new_pos = self.rect.move(self.speed)
		self.rect = new_pos