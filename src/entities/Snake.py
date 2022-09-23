import pygame as pyg
from collections import namedtuple
from ..constants import (
    UP, DOWN, LEFT, RIGHT, TYPE_ERROR_MESSAGE, VALUE_ERROR_MESSAGE,
    CONTENT_TYPE_ERROR_MESSAGE
)

from ..utils import validations

Square = namedtuple('Square', ['x', 'y'])
SNAKE_SQUARE = Square(x=10, y=10)


class Snake():

    def __init__(
        self,
        head_initial_position: tuple,
        middle_initial_position: tuple,
        tail_initial_position: tuple,
        skin_dimensions: tuple = SNAKE_SQUARE,
        head_color: tuple = (51, 102, 255),
        body_color: tuple = (51, 153, 255),
        speed: int = 10
    ):
        self.__set_head_initial_position(head_initial_position)
        self.__set_middle_initial_position(middle_initial_position)
        self.__set_tail_initial_position(tail_initial_position)
        self.skin_dimensions = skin_dimensions

        self.head_color = head_color
        self.body_color = body_color

        self.__head_skin = pyg.Surface(self.skin_dimensions)
        self.__head_skin.fill(self.head_color)

        self.__body_skin = pyg.Surface(self.skin_dimensions)
        self.__body_skin.fill(self.body_color)

        self.__body = [
            self.head_initial_position,
            self.middle_initial_position,
            self.tail_initial_position
        ]
        self.__speed = speed
        self.__is_alive = True

    @property
    def head_initial_position(self):
        return self.__head_initial_position

    def __set_head_initial_position(self, head_initial_position: tuple):
        if validations.are_valid_dimensions(head_initial_position):
            self.__head_initial_position = head_initial_position
        else:
            raise TypeError(CONTENT_TYPE_ERROR_MESSAGE.format(
                param='head_initial_position', tp=int)
            )

    @property
    def middle_initial_position(self):
        return self.__middle_initial_position

    def __set_middle_initial_position(self, middle_initial_position: tuple):
        if validations.are_valid_dimensions(middle_initial_position):
            self.__middle_initial_position = middle_initial_position
        else:
            raise TypeError(CONTENT_TYPE_ERROR_MESSAGE.format(
                param='middle_initial_position', tp=int)
            )

    @property
    def tail_initial_position(self):
        return self.__tail_initial_position

    def __set_tail_initial_position(self, tail_initial_position: tuple):
        if validations.are_valid_dimensions(tail_initial_position):
            self.__tail_initial_position = tail_initial_position
        else:
            raise TypeError(CONTENT_TYPE_ERROR_MESSAGE.format(
                param='tail_initial_position', tp=int)
            )

    @property
    def skin_dimensions(self):
        return self.__skin_dimensions

    @skin_dimensions.setter
    def skin_dimensions(self, skin_dimensions: tuple):
        if validations.are_valid_dimensions(skin_dimensions):
            self.__skin_dimensions = skin_dimensions
        else:
            raise TypeError(CONTENT_TYPE_ERROR_MESSAGE.format(
                param='skin_dimensions', tp=int)
            )

    @property
    def head_color(self):
        return self.__head_color

    @head_color.setter
    def head_color(self, head_color: tuple):
        if validations.is_valid_rgb_color(head_color):
            self.__head_color = head_color
        else:
            raise ValueError(VALUE_ERROR_MESSAGE.format(
                param='head_color',
                restr='(0 <= x <= 255, 0 <= x <= 255, 0 <= x <= 255)')
            )

    @property
    def body_color(self):
        return self.__body_color

    @body_color.setter
    def body_color(self, body_color: tuple):
        if validations.is_valid_rgb_color(body_color):
            self.__body_color = body_color
        else:
            raise ValueError(VALUE_ERROR_MESSAGE.format(
                param='body_color',
                restr='(0 <= x <= 255, 0 <= x <= 255, 0 <= x <= 255)')
            )

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool):
        self.__is_alive = is_alive

    @property
    def body(self):
        return self.__body

    @property
    def speed(self):
        return self.__speed

    def increment_speed(self):
        self.__speed += 1

    def set_direction(self, direction: str):
        if direction == UP:
            self.__body[0] = (self.body[0][0],
                              self.body[0][1] - SNAKE_SQUARE.y)
        elif direction == DOWN:
            self.__body[0] = (self.body[0][0],
                              self.body[0][1] + SNAKE_SQUARE.y)
        elif direction == LEFT:
            self.__body[0] = (self.body[0][0] - SNAKE_SQUARE.x,
                              self.body[0][1])
        elif direction == RIGHT:
            self.__body[0] = (self.body[0][0] + SNAKE_SQUARE.x,
                              self.body[0][1])
        else:
            ValueError(
                VALUE_ERROR_MESSAGE.format(
                    param='direction',
                    restr=(
                        "'direction' must be equal to some of these values: "
                        + "'{0}', '{1}', '{2}', '{3}'".format(UP,
                                                              DOWN,
                                                              LEFT,
                                                              RIGHT)
                    )
                )
            )

    def update_location(self, direction: str):
        for i in range(len(self) - 1, 0, -1):
            self.__body[i] = (self.body[i-1][0], self.body[i-1][1])

        self.set_direction(direction)

    def increase_size(self):
        self.body.append((0, 0))

        if len(self) % 4 == 0:
            self.increment_speed()

    def print_snake(self, screen: pyg.Surface):
        if isinstance(screen, pyg.Surface):
            screen.blit(self.__head_skin, self.body[0])

            for pos in self.body[1:]:
                screen.blit(self.__body_skin, pos)
        else:
            raise TypeError(
                TYPE_ERROR_MESSAGE.format(
                    param='screen', tp=pyg.Surface, inst=type(screen)
                )
            )

    def __len__(self):
        return len(self.body)
