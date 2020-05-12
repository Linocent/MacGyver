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
# sound = pygame.mixer.Sound(main_theme)
# sound.play()

level_name = 'labyrinthe.txt'
case_x = 0
case_y = 0
x = 0 # coord en case de mon perso.
y = 0 # coord en case de mon perso.

compt_obj = 0
num_lock_item1 = 0
num_lock_item2 = 0
num_lock_item3 = 0
s = pygame.image.load(SYRINGE_PICTURE)
s.set_colorkey((255, 255, 255))
s = pygame.transform.scale(s, (40, 40))
t = pygame.image.load(PIPE_PICTURE)
t.set_colorkey((255, 255, 255))
t = pygame.transform.scale(t, (40, 40))
e = pygame.image.load(ETHER_PICTURE)
e.set_colorkey((1, 1, 1))
e = pygame.transform.scale(e, (40, 40))
Game_Over = pygame.image.load(GAMEOVER_PICTURE)
Game_Over = pygame.transform.scale(Game_Over, (40*15, 40*16))
You_Win = pygame.image.load(WIN_PICTURE)
You_Win = pygame.transform.scale(You_Win, (40*15, 40*16))

walk_s = 1
walk_e = 1
walk_t = 1
stay_open = 1

while stay_open:
    pygame.time.Clock().tick(30)
    level = Level(level_name)
    level.generate()
    level.show(window)
    Mc = pygame.image.load(HERO_PICTURE)
    Mc = pygame.transform.scale(Mc, (40, 40))
    Position = Mc.get_rect()
    window.blit(counter, (0, SIDE_WINDOW))

    if compt_obj == 0:
        num_lock_item1 = rd.randint(0, len(level.free_coords)-1)
        num_lock_item2 = rd.randint(0, len(level.free_coords) - 1)
        while num_lock_item2 == num_lock_item1:
            num_lock_item2 = rd.randint(0, len(level.free_coords) - 1)
        num_lock_item3 = rd.randint(0, len(level.free_coords) - 1)
        while (num_lock_item3 == num_lock_item1) or (num_lock_item3 == num_lock_item2):
            num_lock_item3 = rd.randint(0, len(level.free_coords) - 1)
        compt_obj = 1

    if walk_s == 1:
        window.blit(s, level.free_coords[num_lock_item1])
    if walk_t == 1:
        window.blit(t, level.free_coords[num_lock_item2])
    if walk_e == 1:
        window.blit(e, level.free_coords[num_lock_item3])
    window.blit(Mc, (x, y))
    if (x, y) == level.free_coords[num_lock_item1]:
        walk_s = 0
    if walk_s == 0:
        (window.blit(s, (360, 600)))
    if (x, y) == level.free_coords[num_lock_item2]:
        walk_t = 0
    if walk_t == 0:
        (window.blit(t, (420, 600)))
    if (x, y) == level.free_coords[num_lock_item3]:
        walk_e = 0
    if walk_e == 0:
        (window.blit(e, (480, 600)))

    for event in pygame.event.get():
        if event.type == QUIT:
            stay_open = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                stay_open = 0

            if (event.key == K_RIGHT) and (case_x+1 < NUMBER_SPRITE_BY_SIDE):
                if level.matwall[case_y, case_x+1] != 0:
                    case_x += 1
                    x = case_x * SIZE_SPRITE
                    Position = Position.move(x, y)
            if (event.key == K_LEFT) and (case_x-1 >= 0):
                if level.matwall[case_y, case_x - 1] != 0:
                    case_x -= 1
                    x = case_x * SIZE_SPRITE
                    Position = Position.move(x, y)
            if (event.key == K_UP) and (level.matwall[case_y-1, case_x] != 0):
                if case_y-1 >= 0:
                    case_y -= 1
                    y = case_y * SIZE_SPRITE
                    Position = Position.move(x, y)
            if (event.key == K_DOWN) and (case_y+1 < NUMBER_SPRITE_BY_SIDE):
                if level.matwall[case_y + 1, case_x] != 0:
                    case_y += 1
                    y = case_y * SIZE_SPRITE
                    Position = Position.move(x, y)
        pygame.display.flip()

        if level.matwall[case_x, case_y] == 2:
            if (walk_s == 0) and (walk_e == 0) and (walk_t == 0):
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
                """
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                Mc.position('up')
            elif event.key == K_DOWN:
                Mc.direction('down')
            elif event.key == K_RIGHT:
                Mc.direction('right')
            elif event.key == K_LEFT:
                Mc.direction('left')
    pygame.display.flip()
    """