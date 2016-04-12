from octopus import Octopus
import os
from projectile import Sushi
import pygame
from pygame.locals import *
import sys
from whale import Whale

class GameState:
	
	def __init__(self):
		print("INIT SUPER")
		pygame.init()
		self.size = self.width, self.height = 750, 500
		self.screen = pygame.display.set_mode(self.size)

	def handle_event(self, event):
		if event.type == QUIT:
			sys.exit()

	def update(self):
		pass

class StartState(GameState): 
	
	def __init__(self):
		super().__init__()
		self.start_screen = pygame.image.load("startscreen.png").convert()
		self.play_button = pygame.image.load("playbutton.png").convert()
		self.button_rect = self.play_button.get_rect(center=(self.width/2, 3*self.height/4))
	
	def update(self):
		self.screen.blit(self.start_screen, (0,0))
		self.screen.blit(self.play_button, self.button_rect.topleft)
		pygame.display.update()

	def handle_event(self, event):
		super().handle_event(event)
		if event.type == MOUSEBUTTONDOWN:
			event.pos = 0

class LevelOne(GameState):
	
	def __init__(self):
		super().__init__()
		self.color = 210, 210, 210 
		self.whale = Whale()
		self.octopus = Octopus()
		
		self.player_sprite = pygame.sprite.Group(self.whale)
		self.enemy_sprites = pygame.sprite.Group(self.octopus)
		
		self.player_projectiles = pygame.sprite.Group()
		self.enemy_projectiles = pygame.sprite.Group()
		
		self.sprites = pygame.sprite.Group(self.player_sprite, self.enemy_sprites, self.player_projectiles, self.enemy_projectiles)
	
	def handle_event(self, event):
			super().handle_event(event)

			if event.type == KEYDOWN:
				if event.key == K_UP or event.key == K_w:
					self.whale.state = 'moveup'
				if event.key == K_DOWN or event.key == K_s:
					self.whale.state = 'movedown'
				if event.key == K_LEFT or event.key == K_a:
					self.whale.state = 'moveleft'
				if event.key == K_RIGHT or event.key == K_d:
					self.whale.state = 'moveright'

			elif event.type == KEYUP:
				if (event.key == K_UP or event.key == K_w) and self.whale.state == 'moveup':
					self.whale.state = 'still'
				if (event.key == K_DOWN or event.key == K_s) and self.whale.state == 'movedown':
					self.whale.state = 'still'
				if (event.key == K_LEFT or event.key == K_a) and self.whale.state == 'moveleft':
					self.whale.state = 'still'
				if (event.key == K_RIGHT or event.key == K_d) and self.whale.state == 'moveright':
					self.whale.state = 'still'

			elif event.type == MOUSEBUTTONDOWN:
				self.whale.spouting = True
				if self.whale.facing_right:
					launch_location = self.whale.rect.right
				else:
					launch_location = self.whale.rect.left
				bullet = Sushi(self.whale.facing_right, launch_location, self.whale.rect.top+(self.whale.rect.height/2))
				bullet_sprite = pygame.sprite.Group(bullet)
				self.player_projectiles.add(bullet_sprite)
				self.sprites.add(bullet_sprite)
		
	def update(self):
		
		self.screen.fill(self.color)
		self.sprites.update()
		self.sprites.draw(self.screen)
		player_projectile_list = self.player_projectiles.sprites()

		for projectile in player_projectile_list:
			for enemy in self.enemy_sprites.sprites():
				if pygame.sprite.collide_rect(projectile, enemy): #kill any enemy and bullet sprites that collide
					projectile.kill()
					enemy.health -= projectile.damage
					if enemy.health <= 0:
						enemy.kill()


		pygame.display.update()
