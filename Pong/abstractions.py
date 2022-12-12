import pygame
from pygame.locals import *


class Ball:

    def __init__(self, x, y , rad, color=(0, 0, 255)):
        self.pos = [x, y]
        self.rad = rad
        self.color = color
        self.rect = None

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.pos, self.rad)
