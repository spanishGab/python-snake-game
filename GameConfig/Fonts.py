import pygame as pyg
from pygame.locals import *
from GameConfig.config import UP, DOWN

class Fonts():

    def __init__(self, text, style, size, pos, color=(255,255,255)):
        self.set_style(style)
        self.set_size(size)
        self.set_text(text)
        self.set_color(color)
        self.set_type()
        self.set_render()
        self.set_area()
        self.set_location(mid=pos[0], top=pos[1])

    def set_text(self, text):
        self._text = str(text)
    
    def set_style(self, style):
        self._style = style
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = int(size)
        else:
            raise ValueError("'size' parameter must be an integer")
    
    def set_color(self, color): 
        if isinstance(color[0], int) and isinstance(color[1], int) and isinstance(color[2], int):
            if ((color[0] <= 255 and color[0] >= 0) and 
                (color[1] <= 255 and color[1] >= 0) and 
                (color[2] <= 255 and color[2] >= 0)):
                self._color = color
            else:
                raise ValueError("'colors' must be a tuple of integers with the RGB pattern")
        else:
            raise ValueError("'colors' must be a tuple of integers")

    def set_type(self):
        self._font_type = pyg.font.SysFont(self._style, self._size)
    
    def set_render(self, antialias=True):
        self._font_render = self._font_type.render(self._text, antialias, self._color)
    
    def set_area(self):
        self._font_area = self._font_render.get_rect()

    def set_location(self, mid, top=None, left=None, bottom=None, right=None):
        if top:
            self._font_area.midtop = (mid, top)
        elif left:
            self._font_area.midleft = (mid, left)
        elif bottom:
            self._font_area.midbottom = (mid, bottom)
        elif right:
            self._font_area.midright = (mid, right)
        else:
            raise TypeError("Excpected an int, got Nonetype")
    
    def print_font(self, screen):
        screen.blit(self._font_render, self._font_area)

    def alter_color(self, color):
        self.set_color(color)
        self.set_render()

    
        

    
