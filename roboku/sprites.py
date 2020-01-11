from setts import *
import random

class RoboKu(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		PIC = pg.image.load(path.join(PICSFOLDER,'brawlbot_idle_preview.gif')).convert_alpha()
		self.image = pg.transform.scale(PIC, (TILESIZE,TILESIZE))
		#self.image = pg.Surface((TILESIZE,TILESIZE))
		#self.image.fill(MENUCOL)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.lastShot = [pg.time.get_ticks(),pg.time.get_ticks(),pg.time.get_ticks()]#respectively for img,txt,move in drunk meth

	def move(self, dx=0, dy=0):
		if not self.collision(dx, dy):
			self.x += dx
			self.y += dy

	def collision(self, dx=0, dy=0):
		for obstacle in self.game.obstacles:
			#	trying to step on an obstacle	#
			if obstacle.x == self.x + dx and obstacle.y == self.y + dy:
				if obstacle in self.game.waters:
					#	CRY SEEING WATER	#
					if 0 <= self.game.score <= 2:
						self.game.draw_text(self.game.screen,"I cannot swim!", WHITE, 20, self.rect.x+TILESIZE/2, self.rect.y-TILESIZE/4)
					if 3 <= self.game.score <= 4:
						self.game.draw_text(self.game.screen,"Have to be careful!", WHITE, 20, self.rect.x+TILESIZE/2, self.rect.y-TILESIZE/4)
					if 5 <= self.game.score <= 6:
						self.game.draw_text(self.game.screen,"Oups, almost in!", WHITE, 20, self.rect.x+TILESIZE/2, self.rect.y-TILESIZE/4)
					if len(self.game.items) == 0:
						self.game.draw_text(self.game.screen,"OH CRAP!", RED, 61, self.rect.x+TILESIZE/2, self.rect.y-TILESIZE/4)
						self.game.draw_text(self.game.screen,"OH CRAP!", WHITE, 60, self.rect.x+TILESIZE/2, self.rect.y-TILESIZE/4)
						pg.display.update()
						zzz(0.9)
						pg.event.clear()
						self.game.loose()
					pg.display.update()
					zzz(0.25)
					#pg.event.clear()
				return True
		return False

#	def drunk(self):
#		now = pg.time.get_ticks()
#		def knurd(message,delay,drunkedom = False):
#			if (now-self.lastShot[0]) == delay:
#				self.scotoma = (random.randrange(0, WIDTH-TILESIZE), random.randrange(0, HEIGHT-TILESIZE))
#				#scotomax = random.randrange(0, WIDTH-TILESIZE)#scotomay = random.randrange(0, HEIGHT-TILESIZE)
#			if (now-self.lastShot[1]) == delay:
#				self.repercussion = self.rect.x+random.randrange(-TILESIZE/2, TILESIZE/2), self.rect.y+random.randrange(-TILESIZE/2, TILESIZE)
#				#repercussionx = self.rect.x+random.randrange(-TILESIZE/2, TILESIZE/2)#repercussiony = self.rect.y+random.randrange(-TILESIZE/2, TILESIZE)
#
#			if (now-self.lastShot[0]) > delay:
#				##self.game.screen.blit(pg.transform.scale(pg.image.load(path.join(PICSFOLDER,'haakbier.gif')).convert_alpha(),(TILESIZE,TILESIZE)),(random.randrange(-TILESIZE, WIDTH-TILESIZE),random.randrange(-TILESIZE, HEIGHT-TILESIZE)))
#				#scotoma = (random.randrange(0, WIDTH-TILESIZE),random.randrange(0, HEIGHT-TILESIZE))
#				if now-self.lastShot[0] < delay+delay/2:
#					self.game.screen.blit(pg.transform.scale(pg.image.load(path.join(PICSFOLDER,'haakbier.gif')).convert_alpha(),(TILESIZE,TILESIZE)),self.scotoma)
#					#self.game.screen.blit(pg.transform.scale(pg.image.load(path.join(PICSFOLDER,'haakbier.gif')).convert_alpha(),(TILESIZE,TILESIZE)),(scotomax,scotomay))
#				if now-self.lastShot[0] == delay+delay/2:
#					self.lastShot[0] = now
#				#pg.display.flip()
#
#			if (now-self.lastShot[1]) > (delay+50):
#				#repercussion = self.game.draw_text(self.game.screen, message, WHITE, 20, self.rect.x+random.randrange(-TILESIZE/2, TILESIZE/2), self.rect.y+random.randrange(-TILESIZE/2, TILESIZE))
#				if now-self.lastShot[1] < delay+delay+50:
#					self.game.draw_text(self.game.screen, message, WHITE, 20, self.repercussion)
#					#self.game.draw_text(self.game.screen, message, WHITE, 20, repercussionx, repercussiony)
#				if now-self.lastShot[1] == delay+delay+50:
#					self.lastShot[1] = now
#				#pg.display.flip()
#
#			if drunkedom and ((now-self.lastShot[2]) > (2*delay)):
#				self.lastShot[2] = now
#				self.move(random.randrange(-1,1,1),random.randrange(-1,1,1))
#			pg.display.flip()
#
#		if 0 <= self.game.score <= self.game.maxscore*0.4:#[]0 to []30% 7:{0,1,2}
#			pass
#		else:
#			if self.game.maxscore*0.4 < self.game.score < self.game.maxscore*0.7:#()30% to ()60% 7:{3,4}
#				message = ""
#				knurd(message,500)
#			if self.game.maxscore*0.7 <= self.game.score < self.game.maxscore:#[]60% to ()100% 7:{5,6}
#				message = "HIK!"
#				knurd(message,250)
#			if len(self.game.items) == 0:
#			#if (self.game.maxscore - 1) < self.game.score < (self.game.maxscore):
#				message = "Am so drunk..."
#				knurd(message,200,True)
#
	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

class Item(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.items
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		PIC = pg.image.load(path.join(PICSFOLDER,'haakbier.gif')).convert_alpha()
		self.image = pg.transform.scale(PIC, (TILESIZE,TILESIZE))
		#self.image = pg.Surface((TILESIZE,TILESIZE))
		#self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

class Door(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.obstacles, game.wins
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		PIC = pg.image.load(path.join(PICSFOLDER,'castledoors.png')).convert()
		self.image = pg.transform.scale(PIC, (TILESIZE,TILESIZE))
		#self.image = pg.Surface((TILESIZE,TILESIZE))
		#self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.obstacles
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		PIC = pg.image.load(path.join(PICSFOLDER,'wall.png')).convert()
		self.image = pg.transform.scale(PIC, (TILESIZE,TILESIZE))
		#self.image = pg.Surface((TILESIZE,TILESIZE))
		#self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

class Bush(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.obstacles
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		PIC = pg.image.load(path.join(PICSFOLDER,'tile_019.png')).convert_alpha()
		self.image = pg.transform.scale(PIC, (TILESIZE,TILESIZE))
		#self.image = pg.Surface((TILESIZE,TILESIZE))
		#self.image.fill(BUSHCOL)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

class Pond(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.obstacles, game.waters
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		PIC = pg.image.load(path.join(PICSFOLDER,'sea.png')).convert_alpha()
		self.image = pg.transform.scale(PIC, (TILESIZE,TILESIZE))
		#self.image = pg.Surface((TILESIZE,TILESIZE))
		#self.image.fill(PONDCOL)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE
