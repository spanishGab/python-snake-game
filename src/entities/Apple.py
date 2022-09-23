import random
import pygame as pyg

from ..constants import (
    TYPE_ERROR_MESSAGE, VALUE_ERROR_MESSAGE, CONTENT_TYPE_ERROR_MESSAGE,
    SCREEN_WIDTH, SCREEN_HEIGHT
)

from ..utils import validations

APPLE_POSITION_OUT_OF_BONDS = (
    "The apple position given is out of bonds, "
    + "valid values are:"
    + '\n'+'\t'
    + "- for x axis: {min_x} <= x <= {max_x}, "
    + "for y axis: {min_y} <= x <= {max_y}, got "
    + "x = {app_pos_x}, y = {app_pos_y}"
)

X_AXIS_MINIMUM_POSITION = 10
Y_AXIS_MINIMUM_POSITION = 10


class Apple():

    def __init__(
        self,
        dimensions: tuple = (X_AXIS_MINIMUM_POSITION, Y_AXIS_MINIMUM_POSITION),
        color: tuple = (255, 0, 0)
    ):
        self.dimensions = dimensions
        self.color = color
        self.generate_new_random_apple_position()

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: tuple):
        if validations.are_valid_dimensions(dimensions):
            self.__dimensions = pyg.Surface(dimensions)
        else:
            raise ValueError(
                VALUE_ERROR_MESSAGE.format(
                    param='dimensions',
                    restr="'dimensions' must contain only integer elements"
                )
            )

    @property
    def apple_position(self):
        return self.__apple_position

    @apple_position.setter
    def apple_position(self, apple_position: tuple):
        if isinstance(apple_position, tuple):
            if all(isinstance(pos, int) for pos in apple_position):
                if (
                    apple_position[0] >= X_AXIS_MINIMUM_POSITION
                    and apple_position[0] <= SCREEN_WIDTH - 20
                    and apple_position[1] <= SCREEN_HEIGHT - 20
                    and apple_position[1] >= Y_AXIS_MINIMUM_POSITION
                ):
                    self.__apple_position = apple_position
                else:
                    raise ValueError(
                        APPLE_POSITION_OUT_OF_BONDS.format(
                            min_x=X_AXIS_MINIMUM_POSITION,
                            max_x=SCREEN_WIDTH,
                            min_y=Y_AXIS_MINIMUM_POSITION,
                            max_y=SCREEN_HEIGHT,
                            app_pos_x=apple_position[0],
                            app_pos_y=apple_position[1]
                        )
                    )
            else:
                raise TypeError(
                    CONTENT_TYPE_ERROR_MESSAGE.format(param='apple_position',
                                                      tp=int)
                )
        else:
            raise TypeError(
                TYPE_ERROR_MESSAGE.format(
                    param='apple_position', tp=str, inst=type(apple_position)
                )
            )

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: tuple):
        if validations.is_valid_rgb_color(color):
            self.__color = color
        else:
            raise ValueError(VALUE_ERROR_MESSAGE.format(
                param='color',
                restr='(0 <= x <= 255, 0 <= x <= 255, 0 <= x <= 255)')
            )

    def generate_new_random_apple_position(self):
        x = random.randint(X_AXIS_MINIMUM_POSITION, SCREEN_WIDTH - 20)
        y = random.randint(Y_AXIS_MINIMUM_POSITION, SCREEN_HEIGHT - 20)

        self.apple_position = (
            x // X_AXIS_MINIMUM_POSITION * X_AXIS_MINIMUM_POSITION,
            y // Y_AXIS_MINIMUM_POSITION * Y_AXIS_MINIMUM_POSITION
        )
