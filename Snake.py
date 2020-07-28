import pygame as pyg
from config import UP, DOWN, LEFT, RIGHT

class Snake():

    def __init__(self, head, mid, tail, dimensions=(10,10), head_color=(51, 102, 255), body_color=(51, 153, 255), speed=10):
        self.head = head
        self.mid = mid
        self.tail = tail

        self._head_skin = pyg.Surface(dimensions)
        self._body_skin = pyg.Surface(dimensions)
        self.set_skin(head_color, body_color)
        
        self._snake = [head, mid, tail]
        self._speed = speed

    def set_skin(self, head_color, body_color):
        self._head_skin.fill(head_color)
        self._body_skin.fill(body_color)

    def get_snake(self):
        return self._snake

    def get_speed(self):
        return self._speed
    
    def set_speed(self):
        self._speed += 1

    def get_size(self):
        return len(self._snake)

    def set_direction(self, direction):
        if direction == UP:
            self._snake[0] = (self._snake[0][0], self._snake[0][1] - 10)
        elif direction == DOWN:
            self._snake[0] = (self._snake[0][0], self._snake[0][1] + 10)
        elif direction == LEFT:
            self._snake[0] = (self._snake[0][0] - 10, self._snake[0][1])
        elif direction == RIGHT:
            self._snake[0] = (self._snake[0][0] + 10, self._snake[0][1])

    def update_location(self, direction):
        for i in range(self.get_size() - 1, 0, -1):
            self._snake[i] = (self._snake[i-1][0], self._snake[i-1][1])
        
        self.set_direction(direction)
        
    def increase_size(self):
        self._snake.append((0,0))
        
        if self.get_size() % 8 == 0:
            self.set_speed()

    def print_snake(self, screen):
        screen.blit(self._head_skin, self._snake[0])
        
        for pos in self._snake[1:]:
            screen.blit(self._body_skin, pos)


