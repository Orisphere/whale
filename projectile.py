import pygame


class Projectile(pygame.sprite.DirtySprite):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
		self.damage = 10



class Sardine(Projectile):

	def __init__(self, is_facing_right, init_coord_x, init_coord_y):
		Projectile.__init__(self)
		self.image = pygame.image.load('sardine.gif').convert()
		self.rect = self.image.get_rect()
		self.rect.top = init_coord_y
		self.damage = 10

		if is_facing_right:
			self.speed = [10, 0]
			self.rect.right = init_coord_x
		else:
			self.image = pygame.transform.flip(self.image, True, False)
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

#level 1 upgraded projectile
#Twice as fast as Sardines
class Sushi(Projectile):

	def __init__(self, is_facing_right, init_coord_x, init_coord_y):
		Projectile.__init__(self)
		self.image = pygame.image.load('sushi.gif').convert()
		self.rect = self.image.get_rect()
		self.rect.top = init_coord_y
		self.damage = 10

		if is_facing_right:
			self.speed = [20, 0]
			self.rect.right = init_coord_x
		else:
			self.speed = [-20, 0]
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