import pygame
from pygame.locals import *
import operator
import sys
import os

import random
import math
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

 # ships's walking speed
def AddVectors(v1,v2):
    return list(map(operator.add,v1,v2))

DIRECTIONS = {
    "UP": [0, -10],
    "DOWN": [0, 0.5],
    "RIGHT" : [0.95, 0],
    "LEFT" : [-0.95, 0]
}

img_dir = os.path.join(os.path.dirname(__file__), 'resources')
math_dir = os.path.join(os.path.dirname(__file__), 'Math')

class Button:
    def __init__(self, surface, text, font_size, color, x, y, width=None, height=None, callback=None):
        self.surface = surface
        self.text = text
        self.font = pygame.font.SysFont(None, font_size)
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.callback = callback

    def draw(self):
        text_surface = self.font.render(self.text, True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)
        pygame.draw.rect(self.surface, self.color, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20), border_radius=10)
        pygame.draw.rect(self.surface, (255, 255, 255), (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20), border_radius=10, width=5)
        self.surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and self.is_hovered():
            if self.callback:
                self.callback()

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.width is None or self.height is None:
            text_surface = self.font.render(self.text, True, self.color)
            text_rect = text_surface.get_rect()
            self.width = text_rect.width + 20
            self.height = text_rect.height + 20
        return self.x - self.width / 2 < mouse_pos[0] < self.x + self.width / 2 and self.y - self.height / 2 < mouse_pos[1] < self.y + self.height / 2

class Label:
    def __init__(self, text, font_size, font_color, pos):
        self.font_obj = pygame.font.Font(os.path.join(img_dir,"Foldit-Regular.ttf"),font_size)
        self.font_color = font_color
        self.pos = pos
        self.text = text
        self.text_obj = self.font_obj.render(self.text, True, self.font_color)

    def update_text(self, new_text):
        self.text = new_text
        self.text_obj = self.font_obj.render(self.text, True, self.font_color)

    def draw(self, surface):
        surface.blit(self.text_obj, self.pos)

    def update_pos(self, new_pos):
        self.pos = new_pos
