import random
import pygame as pyg

class Apple():

    def __init__(self, dimensions=(10,10), apple_color=(255,0,0)):
        self._set_apple(dimensions)
        self.set_color(apple_color)
        self.create()
        
    def get_apple(self):
        return self._apple
    
    def get_apple_pos(self):
        return self._apple_pos
    
    def get_color(self):
        return self._color

    def _set_apple(self, dimensions):
        if isinstance(dimensions[0], int) and isinstance(dimensions[1], int):
            self._apple = pyg.Surface(dimensions)
        else:
            raise ValueError("'colors' must be a tuple of integers")

    def set_color(self, apple_color):
        if isinstance(apple_color[0], int) and isinstance(apple_color[1], int) and isinstance(apple_color[2], int):
            if ((apple_color[0] <= 255 and apple_color[0] >= 0) and 
                (apple_color[1] <= 255 and apple_color[1] >= 0) and 
                (apple_color[2] <= 255 and apple_color[2] >= 0)):
                self._color = apple_color
                self._apple.fill(apple_color)
            else:
                raise ValueError("'colors' must be a tuple of integers with the RGB pattern")
        else:
            raise ValueError("'colors' must be a tuple of integers")

    def create(self):
        x = random.randint(10,580)
        y = random.randint(10,580)
        self._apple_pos = (x // 10 * 10, y // 10 * 10)
