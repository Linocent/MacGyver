# !/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Help Mac Gyver the game
We must to take item and go to guardian to deliver Mac Gyver

Script Python
files: game.py, level.py, hero.py, constant.py, labyrinthe.txt.
folder: ressource"""

import pygame
from level import Level
from constant import SIDE_WINDOW, TITLE_WINDOW, SIZE_SPRITE, MAIN_THEME
from hero import Hero


# pylint: disable=no-member
# Error of compatibility between pygame and pylint.

pygame.init()

window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW + SIZE_SPRITE))
pygame.display.set_caption(TITLE_WINDOW)
sound = pygame.mixer.Sound(MAIN_THEME)
sound.play()

LEVEL_NAME = 'labyrinthe.txt'

mc = Hero()
level = Level(LEVEL_NAME)
level.generate()


def game():

    stay_open = 1
    while stay_open == 1:
        pygame.time.Clock().tick(30)
        level.show_map(window, mc)
        level.show_item(window, mc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stay_open = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stay_open = 0
                elif event.key == pygame.K_UP:
                    mc.move('up', level)
                elif event.key == pygame.K_DOWN:
                    mc.move('down', level)
                elif event.key == pygame.K_RIGHT:
                    mc.move('right', level)
                elif event.key == pygame.K_LEFT:
                    mc.move('left', level)
            pygame.display.flip()
            stay_open = level.end_screen(window, mc, stay_open)


if __name__ == '__main__':
    game()
