"""class of the game"""

import pygame
from pygame.locals import *
from Constant import *


class Level:
    def __init__(self, files):
        self.files = files
        self.structure = 0

    def generate(self):
        strlab = open(self.files, "r")
        lablines = strlab.read()
        lablines = lablines.split("\n")
        for k in range(len(lablines)):
            lablines[k] = lablines[k][0:len(lablines[k]) - 2]
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
                if Char == 'm':
                    window.blit(Wall, (x,y))
                elif (Char == '0') or (Char == 'd'):
                    window.blit(Floor, (x,y))
                elif Char == 'a':
                    window.blit(Gardian, (x,y))
                num_case += 1
            num_line += 1



class Hero:
    def __init__(self):
        self.hero = pygame.image.load(hero_picture).convert_alpha()
        self.case_x = 1
        self.case_y = 1
        self.x = 21
        self.y = 21

