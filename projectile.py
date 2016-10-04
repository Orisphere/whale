import os
import pygame

# formerly child of pygame.sprite.DirtySprite
class Projectile():
	def __init__(self):
		#pygame.sprite.DirtySprite.__init__(self)
		self.damage = 10
		self.speed = 10
		image_path = os.path.join(os.path.realpath(''), 'Images', 'sardine.gif')
		self.image = pygame.image.load(image_path).convert()

	def fire(self, is_facing_right, init_coord_x, init_coord_y):
		sprite = ProjectileSprite()
		sprite.image = self.image #pygame.image.load('sardine.gif').convert()
		sprite.rect = sprite.image.get_rect()
		sprite.rect.top = init_coord_y
		sprite.damage = self.damage
		if is_facing_right:
			sprite.speed = [self.speed, 0]
			sprite.rect.right = init_coord_x
		else:
			sprite.image = pygame.transform.flip(sprite.image, True, False)
			sprite.speed = [-self.speed, 0]
			sprite.rect.left = init_coord_x
		return sprite

class ProjectileSprite(pygame.sprite.DirtySprite):
	def __init__(self):
		super().__init__()


	def update(self):
		self.move()

	def move(self):
		if self.rect.top < 0 or self.rect.bottom > 500:
			self.kill()
		
		if self.rect.right > 750 or self.rect.left < 0:
			self.kill()
		else:
			new_pos = self.rect.move(self.speed)
			self.rect = new_pos

#, is_facing_right, init_coord_x, init_coord_y
class Sardine(Projectile):

	def __init__(self):
		super().__init__()
		image_path = os.path.join(os.path.realpath(''), 'Images', 'sardine.gif')
		self.image = pygame.image.load(image_path).convert()
		self.damage = 10
		self.speed = 10


#level 1 upgraded projectile
#Twice as fast as Sardines
class Sushi(Projectile):

	def __init__(self):
		super().__init__()
		image_path = os.path.join(os.path.realpath(''), 'Images', 'sushi.gif')
		self.image = pygame.image.load(image_path).convert()
		self.damage = 15
		self.speed = 20




class Dory(Projectile):

	def __init__(self):
		super().__init__()
		image_path = os.path.join(os.path.realpath(''), 'Images', 'dory.gif')
		self.image = pygame.image.load(image_path).convert()
		self.damage = 50
		self.speed = 5
