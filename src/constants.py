from pathlib import Path
import pygame

# Directories and files
RESOURCES_DIR = Path(Path.cwd(), 'resources')
GAME_SOUNDS_DIR = Path(RESOURCES_DIR).joinpath('game_sounds')


# Pygame constants
GARDEN_SCREEN_COLOR = (51, 204, 51)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_VOLUME = 0.03

CLOCK = pygame.time.Clock()

# Game directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Error Messages
NOT_A_RGB_VALUE_ERROR_MESSAGE = (
    "The given value {val} is not a valid rgb "
    + "color component, it must be in range 0 <= x <= 255"
)

TYPE_ERROR_MESSAGE = (
    "The '{param}' must be an instance of {tp} type(s), got {inst}"
)

CONTENT_TYPE_ERROR_MESSAGE = (
    "The '{param}' must contain elements of type {tp}, "
    + "got an element of another type inside of it"
)

VALUE_ERROR_MESSAGE = (
    "The '{param}' must only contain values that respect the "
    + "restriction: '{restr}'"
)

# Font styles
FREE_SANS_BOLD_FONT = "freesansbold.ttf"
PIXELED_FONT = "pixeled.ttf"
