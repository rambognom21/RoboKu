import pygame as pg
from os import path
from time import sleep as zzz

# colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MENUCOL = (225,153,51)
BUTTCOL = (204,102,0)
BUTTSHADOWCOL = (153,76,0)
TITLECOL = (225,153,51)
TITLESHADCOL = (204,102,0)
#UNDERTITLECOL = ()
GRASSCOL = (102,204,0)
GRASSSHADCOL = (0,102,0)
BUSHCOL = (76,153,0)
PONDCOL = (0,204,204)

# window and other
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
TILESIZE = 64 # WIDTH/16
#BUTTONH = HEIGHT/12
#BUTTONW = BUTTONH*4

FPS = 60
TITLE = "RoboKu"
BGCOLOR = GRASSCOL

GAMEFOLDER = path.dirname(__file__)
PICSFOLDER = path.join(GAMEFOLDER,'pics')
SNDFOLDER = path.join(GAMEFOLDER,'sound')
