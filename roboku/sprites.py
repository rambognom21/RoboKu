from setts import *

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

	def move(self, dx=0, dy=0):
		if not self.collision(dx, dy):
			self.x += dx
			self.y += dy

	def collision(self, dx=0, dy=0):
		for obstacle in self.game.obstacles:
			if obstacle.x == self.x + dx and obstacle.y == self.y + dy:
				return True
		#WANNA MAKE HIM CRYING SEEING WATER!@#
#		for drop in self.game.waters:
#			if drop.x == self.x + dx and drop.y == self.y + dy:
#				game.draw_text(game.screen,"I cannot swim!", WHITE, 20, WIDTH/2, HEIGHT/2)
#				font_name = pg.font.match_font('arial')
#				font = pg.font.Font(font_name, 20)
#				text_surface = font.render("I cannot swim!", True, WHITE)
#				text_rect = text_surface.get_rect()
#				text_rect.midtop = (WIDTH/2,HEIGHT/2)
#				surf.blit(text_surface, text_rect)
#				pg.display.update()
#				zzz(2)
#				return True
		return False

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

class Item(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.items
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		#PIC = pg.image.load(path.join(PICSFOLDER,'AsteroidBrown.png')).convert_alpha()
		#PIC = pg.image.load(path.join(PICSFOLDER,'Q_x-beerbottleemptydig.png')).convert_alpha()
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
		self.groups = game.all_sprites, game.obstacles
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
