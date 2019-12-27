import sys
from setts import *
from sprites import *

class Game:
	def __init__(self):
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		pg.key.set_repeat(250, 50)#delay,interval
		self.load_map()
		
	def load_map(self):
		self.map = []
		with open(path.join(GAMEFOLDER, 'map.txt'),'rt') as f:#test.txt,map.txt
			self.map = [line.rstrip() for line in f]

	def lvl(self):
		self.stop = False
		self.score = 0
		self.all_sprites = pg.sprite.Group()
		self.obstacles = pg.sprite.Group()	#inability to step on it
		self.waters = pg.sprite.Group()	#cannot swim!
		self.items = pg.sprite.Group()
		self.wins = pg.sprite.GroupSingle()
		for row, tiles in enumerate(self.map):
			for col, tile in enumerate(tiles):
				if tile == 'R':
					self.player = RoboKu(self, col, row)
				if tile == 'D':
					self.door = Door(self, col, row)
				if tile == 'I':
					Item(self, col, row)
				if tile == '#':
					Bush(self, col, row)
				if tile == '~':
					Pond(self, col, row)
				if tile == ']':
					Wall(self, col, row)
#				if tile == ',':
#					Grass(self, col, row)
		self.run()

	def text_Obj(self, text, font):
		textSurface = font.render(text, True, BLACK)
		return textSurface, textSurface.get_rect()

	def draw_text(self, surf, text, color, size, x, y):
		font_name = pg.font.match_font('arial')
		font = pg.font.Font(font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x,y)
		surf.blit(text_surface, text_rect)

	def draw_scoreBar(self, surf, x, y, sco):
		barPic = pg.image.load(path.join(PICSFOLDER,'haakbier.gif')).convert()
		barPic = pg.transform.scale(barPic, (int(TILESIZE/2),int(TILESIZE/2)))
		barPicRect = barPic.get_rect()
		#
		BAR_LENGTH = TILESIZE/2*7
		BAR_HEIGHT = TILESIZE/2
		fill = sco * BAR_LENGTH/7
		outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
		#fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
		#pg.draw.rect(surf, GREEN, fill_rect)
		pg.draw.rect(surf, WHITE, outline_rect, 2)
		for point in range(0,sco):
			self.screen.blit(barPic,(x+point*TILESIZE/2,y))

	def button(self, buttxt,bx,by,bW,bH,activeColor,inactiveColor,action=None):
		mouse = pg.mouse.get_pos()
		click = pg.mouse.get_pressed()
		if bx+bW > mouse[0] > bx and by+bH > mouse[1] > by:
			pg.draw.rect(self.screen, activeColor, (bx,by,bW,bH))
			if click[0] == 1 and action != None:
				action()
		else:
			pg.draw.rect(self.screen, inactiveColor, (bx,by,bW,bH))
		#buttxtFont = pg.font.Font(None,20)
		#buttxtSurf, buttxtRect = self.text_Obj(buttxt, buttxtFont)
		#buttxtRect.center = ( (bx+(bW/2)), (by+(bH/2)) )
		#self.screen.blit(buttxtSurf, buttxtRect)
		self.draw_text(self.screen, buttxt, BLACK, 20, (bx+(bW/2)), (by+(bH/3)))

	def run(self):
		pg.mixer.music.stop()
		pg.mixer.music.load(path.join(SNDFOLDER, 'SylvanWaltzmp3.mp3'))
		pg.mixer.music.set_volume(0.2)
		pg.mixer.music.play(-1)
		while True:
			self.events()
			self.update()
			self.draw()

	def intro(self):
		self.introBool = True
		while self.introBool:
			#pg.event.wait()
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.quit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE:
						self.introBool = False
			self.screen.fill(BLACK)
			introPic = pg.image.load(path.join(PICSFOLDER,'justbeautifulandlem.jpg')).convert()
			#introPic = pg.transform.scale(introPic, (WIDTH,HEIGHT))
			introPicRect = introPic.get_rect()
			introPicRect.midtop = (WIDTH/2, HEIGHT/8)
			self.screen.blit(introPic,introPicRect)
			self.draw_text(self.screen, "Press SPACE to skip", WHITE, 20, WIDTH/2, HEIGHT-20)
			pg.display.update()

	def main(self):
		self.intro()
		pg.mixer.music.load(path.join(SNDFOLDER, 'Ubermenschwav.wav'))
		pg.mixer.music.set_volume(0.2)
		pg.mixer.music.play(-1)
		#pygame.mixer.music.stop()
		self.menu = True
		while self.menu:
			pg.event.wait()
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.quit()
	#			if event.type == pg.KEYDOWN:
	#				if event.key == pg.K_SPACE:
	#					self.stop = False
			#self.screen.fill(WHITE)
			#titleFont = pg.font.Font('freesansbold.ttf',int(HEIGHT*4/14))
			#titleSurf, titleRect = self.text_Obj("RoboKu", titleFont)
			#titleRect.center = ((WIDTH/2),(HEIGHT*3/14))
			#self.screen.blit(titleSurf, titleRect)
			self.screen.fill(BLACK)
			mainPic = pg.image.load(path.join(PICSFOLDER,'justbeautifulandbinary.gif')).convert()
			#introPic = pg.transform.scale(introPic, (WIDTH,HEIGHT))
			mainPicRect = mainPic.get_rect()
			mainPicRect.midtop = (WIDTH/2, HEIGHT/8)
			self.screen.blit(mainPic,mainPicRect)
			self.draw_text(self.screen, "RoboKu", TITLESHADCOL, int(HEIGHT/4-5), (WIDTH/2), (HEIGHT*3/16))
			self.draw_text(self.screen, "RoboKu", TITLECOL, int(HEIGHT/4), (WIDTH/2), (HEIGHT*3/16))

			buttHeight = HEIGHT/12
			buttWidth = buttHeight*4
			self.button('START GAME',(WIDTH-buttWidth)/2,HEIGHT*8/12,buttWidth,buttHeight,BUTTSHADOWCOL,BUTTCOL,self.lvl)
			self.button('EXIT',(WIDTH-buttWidth)/2,HEIGHT*10/12,buttWidth,buttHeight,BUTTSHADOWCOL,BUTTCOL,self.quit)
			#buttHeight = 64
			#buttWidth = buttHeight*4
			#self.button('START GAME', (WIDTH-buttWidth)/2,HEIGHT*2/3,buttWidth,buttHeight,BUTTSHADOWCOL,BUTTCOL,self.lvl)
			#self.button('credits', (WIDTH-buttWidth)/2,HEIGHT*2/3+70,buttWidth,buttHeight,BUTTSHADOWCOL,BUTTCOL)
			#self.button('EXIT', (WIDTH-buttWidth)/2,HEIGHT*2/3+140,buttWidth,buttHeight,BUTTSHADOWCOL,BUTTCOL,self.quit)
			pg.display.update()

	def pause(self):
		pg.event.wait()
		pg.mixer.music.stop()
		pg.mixer.music.load(path.join(SNDFOLDER, 'Ubermenschwav.wav'))
		pg.mixer.music.set_volume(0.2)
		pg.mixer.music.play(-1)
		while self.stop:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.quit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE:
						self.stop = False
						pg.mixer.music.stop()
						pg.mixer.music.load(path.join(SNDFOLDER, 'SylvanWaltzmp3.mp3'))
						pg.mixer.music.set_volume(0.2)
						pg.mixer.music.play(-1)
			self.screen.fill((0,0,0,80))
			self.draw_text(self.screen, "PAUSE", WHITE, 100, WIDTH/2, HEIGHT/2-100)
			self.draw_text(self.screen, "You move with W, S, A, D", WHITE, 20, WIDTH/2, HEIGHT-250)
			self.draw_text(self.screen, "More features in a future", WHITE, 20, WIDTH/2, HEIGHT-220)
			self.draw_text(self.screen, "Press SPACE to resume the game", WHITE, 20, WIDTH/2, HEIGHT-20)
			pg.display.update()

	def win(self):
		while self.stop:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.quit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_ESCAPE:
						self.quit()
#					if event.key == pg.K_RETURN:
						
			self.screen.fill((0,0,0,80))
			self.draw_text(self.screen, "YOU WON", WHITE, 99, WIDTH/2, HEIGHT/2-100)
			self.draw_text(self.screen, "YOU WON", RED, 100, WIDTH/2, HEIGHT/2-100)
#			self.draw_text(self.screen, "Press ENTER to play again or", WHITE, 20, WIDTH/2, HEIGHT-50)
			self.draw_text(self.screen, "Press ESC to exit the window", WHITE, 20, WIDTH/2, HEIGHT-20)
			pg.display.update()

	def loose(self):
		pass

	def quit(self):
		pg.quit()
		sys.exit()

	def update(self):
		#player collects an item
		gotits = pg.sprite.spritecollide(self.player,self.items,True)
		for gotit in gotits:
			self.score+=1
			#if all items gathered (no item in items):
			if len(self.items) == 0:
				self.obstacles.remove(self.door)
				self.wins.add(self.door)
		self.all_sprites.update()
		justonemorestep = pg.sprite.spritecollide(self.player,self.wins,True)

	def draw(self):
		self.screen.fill(BGCOLOR)
		self.all_sprites.draw(self.screen)
		self.draw_text(self.screen, "Press SPACE for pause/help", WHITE, 20, WIDTH/2, HEIGHT-20)
		#self.draw_text(self.screen, str(self.score), WHITE, 50 ,25 ,10)
		self.draw_scoreBar(self.screen, 25, 10, self.score)
		if len(self.items) == 0 and len(self.wins) != 0:
			self.draw_text(self.screen, "The door is opened for you", RED, 59, WIDTH/2,10)
			self.draw_text(self.screen, "The door is opened for you", WHITE, 60, WIDTH/2,10)
		if self.player.x < 0:
			self.stop = True
			self.win()
			#self.draw_text(self.screen, "YOU WON", RED, 100, WIDTH/2, HEIGHT/2-100)
		pg.display.flip()

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
			if event.type == pg.KEYDOWN:
				#if event.key == pg.K_ESCAPE:
				#	self.quit()
				if event.key == pg.K_a:
					self.player.move(dx=-1)
				if event.key == pg.K_d:
					self.player.move(dx=1)
				if event.key == pg.K_w:
					self.player.move(dy=-1)
				if event.key == pg.K_s:
					self.player.move(dy=1)
				if event.key == pg.K_SPACE:
					self.stop = True
					self.pause()

g = Game()
while True:
	g.main()
#	g.lvl()
#	g.run()
