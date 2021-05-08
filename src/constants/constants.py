import os
import pygame

SRC_DIR = os.path.split(os.path.abspath(__file__), '..')

# Pygame constants
SCREEN = pygame.display.set_mode((600,600))

CLOCK = pygame.time.Clock()

# Game directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Error Messages
TYPE_ERROR_MESSAGE = "The '{param}' must be an instance of {tp}, got {inst}"
CONTENT_TYPE_ERROR_MESSAGE = ("The '{param}' must contain elements of type {tp}, "+
                              "got an element of another type inside of it")
VALUE_ERROR_MESSAGE = ("The '{param}' must only contain values that respect the "+
                       "restriction: '{restr}'")

# Font styles
FREE_SANS_BOLD_FONT = "freesansbold.ttf"
PIXELED_FONT = "pixeled.ttf"