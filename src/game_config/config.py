

import pygame
import os
from  Font import Font









def print_snake(screen, font_color, snake_font, i):
    snake_font_screen = snake_font.render('Snake Game', True, font_color)
    snake_font_area = snake_font_screen.get_rect()
    snake_font_area.midtop = ((600 // 2)- 5 + (i*10), 60 - (i*10))
    screen.blit(snake_font_screen, snake_font_area)


