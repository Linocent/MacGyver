"""Class which manage movement of the game."""
import pygame
from constant import HERO_PICTURE, SIZE_SPRITE, NUMBER_SPRITE_BY_SIDE


class Hero:
    """ This class will manage the movement."""

    def __init__(self):
        self.hero = pygame.image.load(HERO_PICTURE)
        self.hero = pygame.transform.scale(self.hero, (SIZE_SPRITE, SIZE_SPRITE))
        self.case_x = 0  # in case
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
