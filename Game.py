# !/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Help Mac Gyver the game
We must to take item and go to guardian to deliver Mac Gyver

Script Python
files: game.py, class.py, Constant.py, labyrinthe.txt, ressource
"""

import pygame
from pygame.locals import *
import mixer
import random as rd
import time

from Classes import *
from Constant import *

pygame.init()

window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW + SIZE_SPRITE))
pygame.display.set_caption(TITLE_WINDOW)
counter = pygame.image.load(COUNTER)
sound = pygame.mixer.Sound(MAIN_THEME)
sound.play()

level_name = 'labyrinthe.txt'


Game_Over = pygame.image.load(GAMEOVER_PICTURE)
Game_Over = pygame.transform.scale(Game_Over, (40*15, 40*16))
You_Win = pygame.image.load(WIN_PICTURE)
You_Win = pygame.transform.scale(You_Win, (40*15, 40*16))
mc = Hero()
level = Level(level_name)
level.generate()
stay_open = 1

while stay_open:
    pygame.time.Clock().tick(30)
    level.show_map(window, mc)
    level.show_item(window, mc)

    for event in pygame.event.get():
        if event.type == QUIT:
            stay_open = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                stay_open = 0
            elif event.key == K_UP:
                mc.move('up', level)
            elif event.key == K_DOWN:
                mc.move('down', level)
            elif event.key == K_RIGHT:
                mc.move('right', level)
            elif event.key == K_LEFT:
                mc.move('left', level)
        pygame.display.flip()
        if level.matwall[mc.case_x, mc.case_y] == 2:
            if (mc.walk_s == 0) and (mc.walk_e == 0) and (mc.walk_t == 0):
                stay_open = 0
                window.blit(You_Win, (0, 0))
                pygame.display.flip()
                time.sleep(5)
                stay_open = 0
                pygame.quit()

            else:
                window.blit(Game_Over, (0, 0))
                pygame.display.flip()
                time.sleep(5)
                stay_open = 0
                pygame.quit()