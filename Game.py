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

from Classes import *
from Constant import *

pygame.init()

window = pygame.display.set_mode((side_window, side_window))
pygame.display.set_caption(title_window)
# sound = pygame.mixer.Sound(main_theme)
# sound.play()

level_name = 'labyrinthe.txt'
case_x = 0
case_y = 0
x = 0
y = 0


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
            if event.key == K_ESCAPE:
                stay_open = 0
            if (event.key == K_RIGHT) and (case_x+1 < number_sprite_by_side):
                if level.matwall[case_y, case_x+1] != 0:
                    case_x += 1
                    x = case_x * size_sprite
                    Position = Position.move(x, y)
            if (event.key == K_LEFT) and (case_x-1 >= 0):
                if level.matwall[case_y, case_x - 1] != 0:
                    case_x -= 1
                    x = case_x * size_sprite
                    Position = Position.move(x, y)
            if (event.key == K_UP) and (level.matwall[case_y-1, case_x] != 0):
                if case_y-1 >= 0:
                    case_y -= 1
                    y = case_y * size_sprite
                    Position = Position.move(x, y)
            if (event.key == K_DOWN) and (case_y+1 < number_sprite_by_side):
                if level.matwall[case_y + 1, case_x] != 0:
                    case_y += 1
                    y = case_y * size_sprite
                Position = Position.move(x, y)
            if level.matwall[case_x, case_y] == 2:
                stay_open = 0
        pygame.display.flip()
    """
    if level.structure[Mc.case_y] and [Mc.case_x] == 'a':
        stay_open = 0

        elif event.type == KEYDOWN:
            if event.key == K_UP:
                Mc.direction('up')
            elif event.type == K_DOWN:
                Mc.direction('down')
            elif event.type == K_RIGHT:
                Mc.direction('right')
            elif event.type == K_LEFT:
                Mc.direction('left')
    pygame.display.flip()
        if level.structure[mc.case_y][mc.case_x] == 'a':
            stay_open = 0
"""
