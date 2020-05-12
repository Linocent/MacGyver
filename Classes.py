"""class of the game"""

import pygame
from pygame.locals import *
from Constant import *
import numpy as np
import random as rd


class Level:
    def __init__(self, files):

        # Var of generate.
        self.files = files
        self.structure = 0
        self.matwall = 0
        self.free_coords = 0

        # Var of show.

        self.WALL = pygame.image.load(WALL_PICTURE)
        self.WALL = pygame.transform.scale(self.WALL, (40, 40))
        self.FLOOR = pygame.image.load(FLOOR_PICTURE)
        self.FLOOR = pygame.transform.scale(self.FLOOR, (40, 40))
        self.GUARDIAN = pygame.image.load(GUARDIAN_PICTURE).convert_alpha()
        self.GUARDIAN = pygame.transform.scale(self.GUARDIAN, (40, 40))

        # Var of items.

        self.s = pygame.image.load(SYRINGE_PICTURE)
        self.s.set_colorkey((255, 255, 255))
        self.s = pygame.transform.scale(self.s, (40, 40))
        self.t = pygame.image.load(PIPE_PICTURE)
        self.t.set_colorkey((255, 255, 255))
        self.t = pygame.transform.scale(self.t, (40, 40))
        self.e = pygame.image.load(ETHER_PICTURE)
        self.e.set_colorkey((1, 1, 1))
        self.e = pygame.transform.scale(self.e, (40, 40))
        self.count_item = 0
        self.num_lock_item1 = 0
        self.num_lock_item2 = 0
        self.num_lock_item3 = 0
        self.counter = pygame.image.load(COUNTER)
        self.item_collected_sound = pygame.mixer.Sound(COLLECT_ITEM)

    # Generate the structure.

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

    # Show the ground, floor, and hero (no item).

    def show_map(self, window, hero_mc):

        num_line = 0
        for line in self.structure:
            num_case = 0
            for Char in line:
                x = num_case * SIZE_SPRITE
                y = num_line * SIZE_SPRITE
                if Char == 'w':
                    window.blit(self.WALL, (x, y))
                elif (Char == '0') or (Char == 'd'):
                    window.blit(self.FLOOR, (x, y))
                elif Char == 'a':
                    window.blit(self.GUARDIAN, (x, y))
                num_case += 1
            num_line += 1

        window.blit(hero_mc.hero, (hero_mc.x, hero_mc.y))

    # Show item on lab.

    def show_item(self, window, Hero):

        # Creation of coords of items.

        if self.count_item == 0:
            self.num_lock_item1 = rd.randint(0, len(self.free_coords) - 1)
            self.num_lock_item2 = rd.randint(0, len(self.free_coords) - 1)
            while self.num_lock_item2 == self.num_lock_item1:
                self.num_lock_item2 = rd.randint(0, len(self.free_coords) - 1)
            self.num_lock_item3 = rd.randint(0, len(self.free_coords) - 1)
            while (self.num_lock_item3 == self.num_lock_item1) or (self.num_lock_item3 == self.num_lock_item2):
                self.num_lock_item3 = rd.randint(0, len(self.free_coords) - 1)
            self.count_item = 1

        # I print if hero didn't walk on item

        if Hero.walk_s == 1:
            window.blit(self.s, self.free_coords[self.num_lock_item1])
        if Hero.walk_t == 1:
            window.blit(self.t, self.free_coords[self.num_lock_item2])
        if Hero.walk_e == 1:
            window.blit(self.e, self.free_coords[self.num_lock_item3])

        # Deleting of item when hero walks on.

        if (Hero.x, Hero.y) == self.free_coords[self.num_lock_item1]:
            if Hero.walk_s == 1:
                self.item_collected_sound.play()
            Hero.walk_s = 0
        if (Hero.x, Hero.y) == self.free_coords[self.num_lock_item2]:
            if Hero.walk_t == 1:
                self.item_collected_sound.play()
            Hero.walk_t = 0
        if (Hero.x, Hero.y) == self.free_coords[self.num_lock_item3]:
            if Hero.walk_e == 1:
                self.item_collected_sound.play()
            Hero.walk_e = 0

        # Print items on counter.

        window.blit(self.counter, (0, SIDE_WINDOW))
        if Hero.walk_s == 0:
            (window.blit(self.s, (360, 600)))
        if Hero.walk_t == 0:
            (window.blit(self.t, (420, 600)))
        if Hero.walk_e == 0:
            (window.blit(self.e, (480, 600)))


class Hero:
    def __init__(self):

        self.hero = pygame.image.load(HERO_PICTURE)
        self.hero = pygame.transform.scale(self.hero, (40, 40))
        self.case_x = 0  # en case
        self.case_y = 0
        self.x = 0  # en pixel
        self.y = 0
        self.walk_s = 1
        self.walk_e = 1
        self.walk_t = 1

    def move(self, direction, Level):

        if (direction == 'right') and (self.case_x + 1 < NUMBER_SPRITE_BY_SIDE):
            if Level.matwall[self.case_y, self.case_x + 1] != 0:
                self.case_x += 1
                self.x = self.case_x * SIZE_SPRITE
        if (direction == 'left') and (self.case_x - 1 >= 0):
            if Level.matwall[self.case_y, self.case_x - 1] != 0:
                self.case_x -= 1
                self.x = self.case_x * SIZE_SPRITE
        if (direction == 'up') and (Level.matwall[self.case_y - 1, self.case_x] != 0):
            if self.case_y - 1 >= 0:
                self.case_y -= 1
                self.y = self.case_y * SIZE_SPRITE
        if (direction == 'down') and (self.case_y + 1 < NUMBER_SPRITE_BY_SIDE):
            if Level.matwall[self.case_y + 1, self.case_x] != 0:
                self.case_y += 1
                self.y = self.case_y * SIZE_SPRITE
