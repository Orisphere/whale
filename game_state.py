from octopus import Octopus
import os
from projectile import Sushi, Sardine, Dory
import pygame
from pygame.locals import *
import sys
from whale import Whale
from jelly import Jelly
from hermit import Hermit

#STATECHANGE is the first userevent of 9
STATECHANGE = USEREVENT+0

class GameState:
	
	def __init__(self):
		pygame.init()
		self.size = self.width, self.height = 750, 500
		self.screen = pygame.display.set_mode(self.size)
		self.doors = []
		self.cleared = False

	def handle_event(self, event):
		if event.type == QUIT:
			sys.exit()

	def is_cleared(self):
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
			if self.button_rect.collidepoint(event.pos):
				startgame_event = pygame.event.Event(STATECHANGE, event_id="levelOne", new_state="LevelOne")
				pygame.event.post(startgame_event)



class LevelOne(GameState):
	
	def __init__(self):
		super().__init__()
		
		self.background = 210, 210, 210 
		self.heart = pygame.image.load('heart.gif').convert()
		self.halfheart = pygame.image.load('halfheart.gif').convert()
		self.healthbar = pygame.sprite.Group()

		self.whale = Whale()
		self.octopus = Octopus()
		self.jelly = Jelly()	
		self.hermit = Hermit()	
		self.enemy_sprites = pygame.sprite.Group([self.hermit, self.octopus, self.jelly])
		
		self.player_projectiles = pygame.sprite.Group()
		self.enemy_projectiles = pygame.sprite.Group()
		
		self.sprites = pygame.sprite.Group(self.whale, self.enemy_sprites, 
						   self.player_projectiles, self.enemy_projectiles, self.healthbar)
		self.update_healthbar()

	def calc_dmg(self):
		player_projectiles = self.player_projectiles
		enemies = self.enemy_sprites
		enemy_hit = pygame.sprite.groupcollide(enemies, player_projectiles, False, True) 
		
		for enemy in enemy_hit.keys():
			for projectile in enemy_hit[enemy]:
				enemy.health -= projectile.damage
				if enemy.health <= 0:
					enemy.kill()

		whale_collide = pygame.sprite.spritecollideany(self.whale, self.enemy_sprites, False)	
		
		if whale_collide:
			if not self.whale.invincible:
				self.whale.invincible = 50
				self.whale.health -= 1
			if self.whale.health <= 0:
				self.whale.kill()

	def update_healthbar(self):
		pos = [0, 0]
		for i in range(int(self.whale.health/2)):
			self.screen.blit(self.heart.copy(), pos)
			pos[0] += 50
		if self.whale.health%2 == 1:
			self.screen.blit(self.halfheart, pos)

	def shoot(self):
		self.whale.spouting = True
		if self.whale.facing_right:
			launch_location = self.whale.rect.right
		else:
			launch_location = self.whale.rect.left
		bullet = Sardine(self.whale.facing_right, launch_location, self.whale.rect.top+(self.whale.rect.height/2))
		bullet_sprite = pygame.sprite.Group(bullet)
		self.player_projectiles.add(bullet_sprite)
		self.sprites.add(bullet_sprite)
	
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
				self.shoot()
				
	def is_cleared(self):
		
		if self.enemy_sprites.sprites() == []:
			self.cleared = True

	def update(self):
		
		self.screen.fill(self.background)
		self.sprites.update()
		self.sprites.draw(self.screen)
		self.calc_dmg()
		self.update_healthbar()
		self.is_cleared()

		if self.cleared: 
			playerwon_event = pygame.event.Event(STATECHANGE, event_id="won", new_state="StartState")
			pygame.event.post(playerwon_event)

		pygame.display.update()
