"""Class of the game"""

import random as rd
import pygame
from constant import *
import numpy as np


class Level:

    """ This class will build the lab and manage items """

    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.
    # pylint: disable=too-many-branches
    # Fifteen is reasonable in this case.

    def __init__(self, files):

        # Var of generate.

        self.files = files
        self.structure = 0
        self.mat_wall = 0
        self.free_coords = 0

        # Var of show.

        self.wall = pygame.image.load(WALL_PICTURE)
        self.wall = pygame.transform.scale(self.wall, (SIZE_SPRITE, SIZE_SPRITE))
        self.floor = pygame.image.load(FLOOR_PICTURE)
        self.floor = pygame.transform.scale(self.floor, (SIZE_SPRITE, SIZE_SPRITE))
        self.guardian = pygame.image.load(GUARDIAN_PICTURE).convert_alpha()
        self.guardian = pygame.transform.scale(self.guardian, (SIZE_SPRITE, SIZE_SPRITE))

        # Var of items1.

        self.syringe = pygame.image.load(SYRINGE_PICTURE)
        self.syringe.set_colorkey((255, 255, 255))
        self.syringe = pygame.transform.scale(self.syringe, (SIZE_SPRITE, SIZE_SPRITE))
        self.pipe = pygame.image.load(PIPE_PICTURE)
        self.pipe.set_colorkey((255, 255, 255))
        self.pipe = pygame.transform.scale(self.pipe, (SIZE_SPRITE, SIZE_SPRITE))
        self.ether = pygame.image.load(ETHER_PICTURE)
        self.ether.set_colorkey((1, 1, 1))
        self.ether = pygame.transform.scale(self.ether, (SIZE_SPRITE, SIZE_SPRITE))
        self.count_item = 0
        self.num_lock_item1 = 0
        self.num_lock_item2 = 0
        self.num_lock_item3 = 0
        self.counter = pygame.image.load(COUNTER)
        self.counter = pygame.transform.scale(self.counter, (SIDE_WINDOW, SIZE_SPRITE))
        self.item_collected_sound = pygame.mixer.Sound(COLLECT_ITEM)

        # var of end screen.

        self.game_over = pygame.image.load(GAME_OVER_PICTURE)
        self.game_over = pygame.transform.scale(self.game_over,
                                                (SIDE_WINDOW, SIDE_WINDOW + SIZE_SPRITE))
        self.you_win = pygame.image.load(WIN_PICTURE)
        self.you_win = pygame.transform.scale(self.you_win,
                                              (SIDE_WINDOW, SIDE_WINDOW + SIZE_SPRITE))

    def generate(self):

        """Generate the structure."""

        str_lab = open(self.files, "r")
        lab_lines = str_lab.read()
        lab_lines = lab_lines.split('\n')
        for k in range(len(lab_lines)):
            lab_lines[k] = lab_lines[k][0:len(lab_lines[k])]
            lab_lines[k] = list(lab_lines[k])
        mat_wall = np.ones([len(lab_lines), len(lab_lines[0])])
        free_coords = []
        for i in range(len(mat_wall[0])):
            for j in range(len(mat_wall[0])):
                if lab_lines[i][j] == 'w':
                    mat_wall[i, j] = 0
                if lab_lines[i][j] == 'a':
                    mat_wall[i, j] = 2
                if lab_lines[i][j] == 'd':
                    mat_wall[i, j] = 3
        for i in range(len(mat_wall[0])):
            for j in range(len(mat_wall[0])):
                if mat_wall[i][j] == 1:
                    free_coords.append((j, i))
        self.mat_wall = mat_wall
        self.structure = lab_lines
        self.free_coords = free_coords
        str_lab.close()

    def show_map(self, window, hero_mc):

        """Show the ground, floor, and hero (no item)."""

        num_line = 0
        for line in self.structure:
            num_case = 0
            for char in line:
                x_map = num_case * SIZE_SPRITE
                y_map = num_line * SIZE_SPRITE
                if char == 'w':
                    window.blit(self.wall, (x_map, y_map))
                elif char in ('0', 'd'):
                    window.blit(self.floor, (x_map, y_map))
                elif char == 'a':
                    window.blit(self.guardian, (x_map, y_map))
                num_case += 1
            num_line += 1

        window.blit(hero_mc.hero, (hero_mc.case_x*SIZE_SPRITE, hero_mc.case_y*SIZE_SPRITE))

    def show_item(self, window, hero):

        """Manage item on lab."""

        # Creation of coords of items.

        if self.count_item == 0:
            self.num_lock_item1 = rd.randint(0, len(self.free_coords) - 1)
            self.num_lock_item2 = rd.randint(0, len(self.free_coords) - 1)
            while self.num_lock_item2 == self.num_lock_item1:
                self.num_lock_item2 = rd.randint(0, len(self.free_coords) - 1)
            self.num_lock_item3 = rd.randint(0, len(self.free_coords) - 1)
            while (self.num_lock_item3 == self.num_lock_item1) or \
                    (self.num_lock_item3 == self.num_lock_item2):
                self.num_lock_item3 = rd.randint(0, len(self.free_coords) - 1)
            self.count_item = 1

        # I print if hero didn't walk on item

        if hero.walk_s == 1:
            tupple1 = self.free_coords[self.num_lock_item1]
            tupple_pix1 = (tupple1[0]*SIZE_SPRITE, tupple1[1]*SIZE_SPRITE)
            window.blit(self.syringe, tupple_pix1)
        if hero.walk_t == 1:
            tupple2 = self.free_coords[self.num_lock_item2]
            tupple_pix2 = (tupple2[0] * SIZE_SPRITE, tupple2[1] * SIZE_SPRITE)
            window.blit(self.pipe, tupple_pix2)
        if hero.walk_e == 1:
            tupple3 = self.free_coords[self.num_lock_item3]
            tupple_pix3 = (tupple3[0] * SIZE_SPRITE, tupple3[1] * SIZE_SPRITE)
            window.blit(self.ether, tupple_pix3)

        # Deleting of item when hero walks on.

        if (hero.case_x, hero.case_y) == self.free_coords[self.num_lock_item1]:
            if hero.walk_s == 1:
                self.item_collected_sound.play()
            hero.walk_s = 0
        if (hero.case_x, hero.case_y) == self.free_coords[self.num_lock_item2]:
            if hero.walk_t == 1:
                self.item_collected_sound.play()
            hero.walk_t = 0
        if (hero.case_x, hero.case_y) == self.free_coords[self.num_lock_item3]:
            if hero.walk_e == 1:
                self.item_collected_sound.play()
            hero.walk_e = 0

        # Print items on counter.

        window.blit(self.counter, (0, SIDE_WINDOW))
        if hero.walk_s == 0:
            (window.blit(self.syringe, (SIZE_SPRITE * 9, SIDE_WINDOW)))
        if hero.walk_t == 0:
            (window.blit(self.pipe, (SIZE_SPRITE * 10.5, SIDE_WINDOW)))
        if hero.walk_e == 0:
            (window.blit(self.ether, (SIZE_SPRITE * 12, SIDE_WINDOW)))

    def end_screen(self, window, m_c, stay_open):

        """choose and show the end screen."""

        if self.mat_wall[m_c.case_x, m_c.case_y] == 2:
            if (m_c.walk_s == 0) and (m_c.walk_e == 0) and (m_c.walk_t == 0):
                window.blit(self.you_win, (0, 0))
                pygame.display.flip()
                pygame.time.delay(3000)

            else:
                window.blit(self.game_over, (0, 0))
                pygame.display.flip()
                pygame.time.delay(3000)
            return 0
        return stay_open


class Hero:

    """ This class will manage the movement."""

    def __init__(self):

        self.hero = pygame.image.load(HERO_PICTURE)
        self.hero = pygame.transform.scale(self.hero, (SIZE_SPRITE, SIZE_SPRITE))
        self.case_x = 0  # en case
        self.case_y = 0
        self.walk_s = 1
        self.walk_e = 1
        self.walk_t = 1

    def move(self, direction, level):

        """Manage movement."""

        if (direction == 'right') and (self.case_x + 1 < NUMBER_SPRITE_BY_SIDE):
            if level.mat_wall[self.case_y, self.case_x + 1] != 0:
                self.case_x += 1
        if (direction == 'left') and (self.case_x - 1 >= 0):
            if level.mat_wall[self.case_y, self.case_x - 1] != 0:
                self.case_x -= 1
        if (direction == 'up') and (level.mat_wall[self.case_y - 1, self.case_x] != 0):
            if self.case_y - 1 >= 0:
                self.case_y -= 1
        if (direction == 'down') and (self.case_y + 1 < NUMBER_SPRITE_BY_SIDE):
            if level.mat_wall[self.case_y + 1, self.case_x] != 0:
                self.case_y += 1

    def give_att(self):

        """None use."""

        print(self.walk_t)
        print(self.walk_e)
        print(self.walk_s)
