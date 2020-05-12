"""class of the game"""

import pygame
from pygame.locals import *
from Constant import *
import numpy as np


class Level:
    def __init__(self, files):
        self.files = files
        self.structure = 0
        self.matwall = 0
        self.free_coords = 0

    def generate(self):
        strlab = open(self.files, "r")
        lablines = strlab.read()
        lablines = lablines.split('\n')
        for k in range(len(lablines)):
            lablines[k] = lablines[k][0:len(lablines[k])]
            lablines[k] = list(lablines[k])
        matwall = np.ones([len(lablines), len(lablines[0])])
        free_coords = []
        for i in range(len(matwall[0])):
            for j in range(len(matwall[0])):
                if lablines[i][j] == 'w':
                    matwall[i, j] = 0
                if lablines[i][j] == 'a':
                    matwall[i, j] = 2
                if lablines[i][j] == 'd':
                    matwall[i, j] = 3
        for i in range(len(matwall[0])):
            for j in range(len(matwall[0])):
                if matwall[i][j] == 1:
                    free_coords.append((j*SIZE_SPRITE, i*SIZE_SPRITE))
        self.matwall = matwall
        self.structure = lablines
        self.free_coords = free_coords
        strlab.close()

    def show(self, window):
        WALL = pygame.image.load(WALL_PICTURE)
        WALL = pygame.transform.scale(WALL, (40, 40))
        FLOOR = pygame.image.load(FLOOR_PICTURE)
        FLOOR = pygame.transform.scale(FLOOR, (40, 40))
        GARDIAN = pygame.image.load(GARDIAN_PICTURE).convert_alpha()
        GARDIAN = pygame.transform.scale(GARDIAN, (40, 40))

        num_line = 0
        for line in self.structure:
            num_case = 0
            for Char in line:
                x = num_case * SIZE_SPRITE
                y = num_line * SIZE_SPRITE
                if Char == 'w':
                    window.blit(WALL, (x, y))
                elif (Char == '0') or (Char == 'd'):
                    window.blit(FLOOR, (x, y))
                elif Char == 'a':
                    window.blit(GARDIAN, (x, y))
                num_case += 1
            num_line += 1


class Hero:
    def __init__(self, level):
        self.hero = pygame.image.load(HERO_PICTURE)
        self.hero = pygame.transform.scale(HERO_PICTURE, (40, 40))
        self.direction = self.window.blit(HERO_PICTURE, (self.x, self.y))
        self.window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.position = self.hero.get_rect()
        self.level = level

    def move(self, direction):
        for event in pygame.event.get():
            if direction == 'right':
                if self.case_x + 1 < NUMBER_SPRITE_BY_SIDE:
                    if self.level.matwall[self.case_y, self.case_x + 1] != 0:
                        self.case_x += 1
                        self.x = self.case_x * SIZE_SPRITE
                        self.position = self.position.move(self.x, self.y)
                if (event.key == K_LEFT) and (self.case_x - 1 >= 0):
                    if self.level.matwall[self.case_y, self.case_x - 1] != 0:
                        self.case_x -= 1
                        self.x = self.case_x * SIZE_SPRITE
                        self.position = self.position.move(self.x, self.y)
                if (event.key == K_UP) and (self.level.matwall[self.case_y - 1, self.case_x] != 0):
                    if self.case_y - 1 >= 0:
                        self.case_y -= 1
                        self.y = self.case_y * SIZE_SPRITE
                        self.position = self.position.move(self.x, self.y)
                if (event.key == K_DOWN) and (self.case_y + 1 < NUMBER_SPRITE_BY_SIDE):
                    if self.level.matwall[self.case_y + 1, self.case_x] != 0:
                        self.case_y += 1
                        self.y = self.case_y * SIZE_SPRITE
                        self.position = self.position.move(self.x, self.y)