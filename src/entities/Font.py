import pygame as pyg

from ..constants import (
    TYPE_ERROR_MESSAGE, VALUE_ERROR_MESSAGE, RESOURCES_DIR,
    FREE_SANS_BOLD_FONT, PIXELED_FONT
)
from ..utils import validations

GAME_FONTS_DIR = RESOURCES_DIR.joinpath('game_fonts')


class Font:

    def __init__(self,
                 text: str,
                 style: str,
                 size: int,
                 position: tuple,
                 color: tuple = (255, 255, 255)):
        self._set_text(text)
        self._set_style(style)
        self._set_size(size)
        self._set_color(color)

        self._set_font_type()
        self._set_font_render()
        self._set_font_area()
        self.set_font_location_by_mid(mid=position[0], top=position[1])

    @property
    def text(self):
        return self.__text

    def _set_text(self, text: str):
        if isinstance(text, str):
            self.__text = text
        else:
            raise TypeError(
                TYPE_ERROR_MESSAGE.format(param='text',
                                          tp=str,
                                          inst=type(text))
            )

    @property
    def style(self):
        return self.__style

    def _set_style(self, style: str):
        if isinstance(style, str):
            style = style.lower()

            if style in (FREE_SANS_BOLD_FONT, PIXELED_FONT):
                self.__style = style
            else:
                raise ValueError(
                    VALUE_ERROR_MESSAGE.format(
                        param='style',
                        restr=(
                            "'style' must be equal to "
                            + "'{0}' or '{1}'"
                        ).format(FREE_SANS_BOLD_FONT,
                                 PIXELED_FONT)
                    )
                )
        else:
            raise TypeError(
                TYPE_ERROR_MESSAGE.format(param='style',
                                          tp=str,
                                          inst=type(style))
            )

    @property
    def size(self):
        return self.__size

    def _set_size(self, size: int):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError(
                TYPE_ERROR_MESSAGE.format(param='size',
                                          tp=int,
                                          inst=type(size))
            )

    @property
    def color(self):
        return self.__color

    def _set_color(self, color: tuple):
        if validations.is_valid_rgb_color(color):
            self.__color = color
        else:
            raise ValueError(VALUE_ERROR_MESSAGE.format(
                param='color',
                restr='(0 <= x <= 255, 0 <= x <= 255, 0 <= x <= 255)')
            )

    @property
    def font_type(self):
        return self.__font_type

    def _set_font_type(self):
        self.__font_type = pyg.font.Font(
            str(GAME_FONTS_DIR.joinpath(self.__style)),
            self.__size
        )

    def _set_font_render(self, antialias: bool = True):
        self.__font_render = self.__font_type.render(self.__text, antialias,
                                                     self.__color)

    def _set_font_area(self):
        self.__font_area = self.__font_render.get_rect()

    def set_font_location_by_mid(self,
                                 mid: int,
                                 top: int = None,
                                 left: int = None,
                                 bottom: int = None,
                                 right: int = None):
        if top:
            self.__font_area.midtop = (mid, top)
        elif left:
            self.__font_area.midleft = (mid, left)
        elif bottom:
            self.__font_area.midbottom = (mid, bottom)
        elif right:
            self.__font_area.midright = (mid, right)
        else:
            raise TypeError(
                "Excpected an <class 'int'> instance for one of the "
                + "params (top, left, bottom, right), got "
                + "<class 'NoneType'> or all of them"
            )

    def print_font(self, screen: pyg.Surface):
        if isinstance(screen, pyg.Surface):
            screen.blit(self.__font_render, self.__font_area)
        else:
            raise TypeError(
                TYPE_ERROR_MESSAGE.format(param='screen',
                                          tp=pyg.Surface,
                                          inst=type(screen))
            )

    def alter_font_color(self, color: tuple):
        self._set_color(color)
        self._set_font_render()

    def alter_font_text(self, text: str):
        self._set_text(text)
        self._set_font_render()
