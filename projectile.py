import pygame


class Projectile(pygame.sprite.DirtySprite):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)

class Sushi(Projectile):

	def __init__(self, is_facing_right, init_coord_x, init_coord_y):
		Projectile.__init__(self)
		self.image = pygame.image.load('projectile.gif').convert()
		self.rect = self.image.get_rect()
		self.rect.top = init_coord_y

		if is_facing_right:
			self.speed = [10, 0]
			self.rect.right = init_coord_x
		else:
			self.speed = [-10, 0]
			self.rect.left = init_coord_x
		# self.start_coord_x = init_coord_x
		# self.start_coord_y = init_coord_y


	def update(self):
		self.move()

	def move(self):
		if self.rect.top < 0 or self.rect.bottom > 500:
			self.kill()
			#self.speed[1] = -self.speed[1]
		
		if self.rect.right > 750 or self.rect.left < 0:
			self.kill()
			#self.speed[0] = -self.speed[0]
		else:
			new_pos = self.rect.move(self.speed)
			self.rect = new_pos
