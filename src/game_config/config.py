

import pygame
import os
from GameConfig.Fonts import Fonts









def print_snake(screen, font_color, snake_font, i):
    snake_font_screen = snake_font.render('Snake Game', True, font_color)
    snake_font_area = snake_font_screen.get_rect()
    snake_font_area.midtop = ((600 // 2)- 5 + (i*10), 60 - (i*10))
    screen.blit(snake_font_screen, snake_font_area)


def switch_title(font, color, pos=None):
    font.alter_font_color(color)

    if pos:
        font.set_font_location_by_mid(mid=pos[0], top=pos[1])

    return font