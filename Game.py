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

from Classes import *
from Constant import *

pygame.init()

window = pygame.display.set_mode((side_window, side_window))
pygame.display.set_caption(title_window)
# sound = pygame.mixer.Sound(main_theme)
# sound.play()

level_name = 'labyrinthe.txt'

s = pygame.image.load(syringe_picture)
s.set_colorkey((255, 255, 255))
s = pygame.transform.scale(s, (40, 40))
t = pygame.image.load(pipe_picture)
t.set_colorkey((255, 255, 255))
t = pygame.transform.scale(t, (40, 40))
e = pygame.image.load(ether_picture)
e.set_colorkey((1, 1, 1))
e = pygame.transform.scale(e, (40, 40))
walk_s = 1
walk_e = 1
walk_t = 1
stay_open = 1
case_x = 0
case_y = 0
x = 0 # coord en case de mon perso.
y = 0 # coord en case de mon perso.

compt_obj = 0
num_lock_item1 = 0
num_lock_item2 = 0
num_lock_item3 = 0
    while stay_open:
        pygame.time.Clock().tick(30)
        level = Level(level_name)
        level.generate()
        level.show(window)
        Mc = pygame.image.load(hero_picture)
        Mc = pygame.transform.scale(Mc, (40, 40))
        Position = Mc.get_rect()

        if compt_obj == 0:
            num_lock_item1 = rd.randint(0, len(level.free_coords)-1)
            # level.free_coords.remove(level.free_coords[num_lock_item1])

            num_lock_item2 = rd.randint(0, len(level.free_coords) - 1)
            # level.free_coords.remove(level.free_coords[num_lock_item2])

            num_lock_item3 = rd.randint(0, len(level.free_coords) - 1)
            # level.free_coords.remove(level.free_coords[num_lock_item3])
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
        if (x, y) == level.free_coords[num_lock_item2]:
            walk_t = 0
        if (x, y) == level.free_coords[num_lock_item3]:
            walk_e = 0

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
                    if (walk_s == 0) and (walk_e == 0) and (walk_t == 0):
                        stay_open = 0
                        loose = 0
                    else:
                        print('Game Over')
            pygame.display.flip()

    """

        elif event.type == KEYDOWN:
            if event.key == K_UP:
                Mc.direction('up')
            elif event.key == K_DOWN:
                Mc.direction('down')
            elif event.key == K_RIGHT:
                Mc.direction('right')
            elif event.key == K_LEFT:
                Mc.direction('left')
    pygame.display.flip()
        if level.structure[mc.case_y][mc.case_x] == 'a':
            stay_open = 0
"""
