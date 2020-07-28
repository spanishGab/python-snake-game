import random
import pygame as pyg

class Apple():

    def __init__(self, dimensions=(10,10), apple_color=(255,0,0)):
        self._apple = pyg.Surface(dimensions)
        self.set_color(apple_color)
        self.create()
        
    def set_color(self, apple_color):
        self._apple.fill(apple_color)

    def get_apple(self):
        return self._apple
    
    def get_apple_pos(self):
        return self._apple_pos

    def create(self):
        x = random.randint(10,580)
        y = random.randint(10,580)
        self._apple_pos = (x // 10 * 10, y // 10 * 10)
