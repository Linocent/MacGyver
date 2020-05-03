# !/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Help Mac Gyver the game
We must to take item and go to guardian to deliver Mac Gyver

Script Python
files: game.py, class.py, Constant.py, level, ressource
"""

import pygame
from pygame.locals import *
import mixer

from Classes import *
from Constant import *

pygame.init()

window = pygame.display.set_mode((side_window, side_window))
pygame.display.set_caption(title_window)
sound = pygame.mixer.Sound(main_theme)
sound.play()

level_name = 'labyrinthe.txt'
case_x = 1
case_y = 1
x = 21
y = 21

stay_open = 1
while stay_open:
    pygame.time.Clock().tick(30)
    level = Level(level_name)
    level.generate()
    level.show(window)
    Mc = pygame.image.load(hero_picture)
    Position = Mc.get_rect()
    window.blit(Mc, (x, y))

    for event in pygame.event.get():
        if event.type == QUIT:
            stay_open = 0
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if [case_y] and [case_x + 1] != 'm':
                    case_x += 1
                    x = case_x * size_sprite
            Position = Position.move(x, y)
            if event.key == K_LEFT:
                if [case_y] and [case_x - 1] != 'm':
                    case_x -= 1
                    x = case_x * size_sprite
            Position = Position.move(x, y)
            if event.key == K_UP:
                if [case_y - 1] and [case_x] != 'm':
                    case_y -= 1
                    y = case_y * size_sprite
            Position = Position.move(x, y)
            if event.key == K_DOWN:
                if [case_y + 1] and [case_x] != 'm':
                    case_y += 1
                    y = case_y * size_sprite
            Position = Position.move(x, y)
    pygame.display.flip()
    """
    if level.structure[Mc.case_y] and [Mc.case_x] == 'a':
        stay_open = 0

        elif event.type == KEYDOWN:
            if event.key == K_UP:
                mc.moove('up')
            elif event.type == K_DOWN:
                mc.moove('down')
            elif event.type == K_RIGHT:
                mc.moove('right')
            elif event.type == K_LEFT:
                mc.moove('left')
    pygame.display.flip()
        if level.structure[mc.case_y][mc.case_x] == 'a':
            stay_open = 0
"""
