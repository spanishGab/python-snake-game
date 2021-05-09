import os
import pygame

# General constants
TRAILING_NEW_LINE = '\n'
TAB_CHARACTER = '\t'
BEST_SCORE_FILE = 'best_score.txt'


# Directories
current_dir, _ = os.path.split(os.path.abspath(__file__))
SRC_DIR = os.path.join(current_dir, '..')
RESOURCES_DIR = os.path.join(SRC_DIR, '..', 'resources')
GAME_FONTS_DIR = os.path.join(RESOURCES_DIR, 'game_fonts')
GAME_SOUNDS_DIR = os.path.join(RESOURCES_DIR, 'game_sounds')
GAME_SCORE_DIR = os.path.join(RESOURCES_DIR, 'game_score')


# Pygame constants
GARDEN_SCREEN_COLOR = (51, 204, 51)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

CLOCK = pygame.time.Clock()

# Game directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Error Messages
NOT_A_RGB_VALUE_ERROR_MESSAGE = ("The given value {val} is not a valid rgb " +
                                 "color component, it must be in range 0 <= x <= 255")

TYPE_ERROR_MESSAGE = "The '{param}' must be an instance of {tp} type(s), got {inst}"

CONTENT_TYPE_ERROR_MESSAGE = ("The '{param}' must contain elements of type {tp}, "+
                              "got an element of another type inside of it")

VALUE_ERROR_MESSAGE = ("The '{param}' must only contain values that respect the "+
                       "restriction: '{restr}'")

# Font styles
FREE_SANS_BOLD_FONT = "freesansbold.ttf"
PIXELED_FONT = "pixeled.ttf"

# Game sounds
HAPPY_CAVE_MUSIC_SOUND = 'happy-cave.ogg'
CARROT_SOUND = 'carrot.ogg'
GAME_OVER_SOUND = 'game-over.ogg'
INTRO_MUSIC_SOUND = 'intro-music.ogg'
ENTER_SOUND = 'enter.ogg'