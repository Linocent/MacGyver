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

    def generate(self):
        strlab = open(self.files, "r")
        lablines = strlab.read()
        lablines = lablines.split('\n')
        for k in range(len(lablines)):
            lablines[k] = lablines[k][0:len(lablines[k])]
            lablines[k] = list(lablines[k])
        matwall = np.ones([len(lablines), len(lablines[0])])
        for i in range(len(matwall[0])):
            for j in range(len(matwall[0])):
                if lablines[i][j] == 'w':
                    matwall[i, j] = 0
                if lablines[i][j] == 'a':
                    matwall[i, j] = 2
                if lablines[i][j] == 'd':
                    matwall[i, j] = 3
        self.matwall = matwall
        self.structure = lablines
        strlab.close()

    def show(self, window):
        Wall = pygame.image.load(wall_picture)
        Floor = pygame.image.load(floor_picture)
        Gardian = pygame.image.load(guardian_picture).convert_alpha()

        num_line = 0
        for line in self.structure:
            num_case = 0
            for Char in line:
                x = num_case * size_sprite
                y = num_line * size_sprite
                if Char == 'w':
                    window.blit(Wall, (x,y))
                elif (Char == '0') or (Char == 'd'):
                    window.blit(Floor, (x,y))
                elif Char == 'a':
                    window.blit(Gardian, (x,y))
                num_case += 1
            num_line += 1


class Hero:
    def __init__(self, level):
        self.hero = self.window.blit(hero_picture, (self.x, self.y))
        self.case_x = 1
        self.case_y = 1
        self.x = 21
        self.y = 21
        self.level = level
        self.position = self.hero.get_rect()

    def moovement(self, position):
        if position == 'right':
            if self.level.structure[self.case_y] and [self.case_x + 1] != 'm':
                self.case_x += 1
                self.x = self.case_x * size_sprite
        self.position = self.position.move(self.case_x, self.case_y)
