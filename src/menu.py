import sys
import pygame
from pygame.locals import QUIT, KEYDOWN
from collections import namedtuple
from .game import play_game
from .entities.Font import Font
from .constants import (
    UP, DOWN, CLOCK, SCREEN, SCREEN_WIDTH, GARDEN_SCREEN_COLOR, PIXELED_FONT,
    GAME_SOUNDS_DIR, GAME_VOLUME
)
from .db import create_best_score_file
from .utils.keyboard import should_go_up, should_go_down, enter_pressed

Colors = namedtuple(
    "Colors",
    [
        'black',
        'white',
        'pool_blue',
        'pink',
        'aqua'
    ]
)

PLAY_FONT_POSITION = ((SCREEN_WIDTH // 2), 160)
QUIT_FONT_POSITION = ((SCREEN_WIDTH // 2), 190)
GAME_TITLE_FONT_POSITION = ((SCREEN_WIDTH // 2) + 5, 50)

BLACK_RGB = (0, 0, 0)
WHITE_RGB = (255, 255, 255)
POOL_BLUE_RGB = (0, 204, 204)
PINK_RGB = (204, 0, 102)
AQUA_RGB = (0, 255, 255)

HIT_ENTER_SOUND = pygame.mixer.Sound(
    str(GAME_SOUNDS_DIR.joinpath('enter.ogg'))
)
HIT_ENTER_SOUND.set_volume(GAME_VOLUME)

INTRO_MUSIC = GAME_SOUNDS_DIR.joinpath('intro-music.ogg')

MENU_COLORS = Colors(
    black=BLACK_RGB,
    white=WHITE_RGB,
    pool_blue=POOL_BLUE_RGB,
    pink=PINK_RGB,
    aqua=AQUA_RGB
)

CURSOR_BLINK_CONFIG = (
    {
        'color': MENU_COLORS.white,
        'position': ((SCREEN_WIDTH // 2) + 5, 50)
    },
    {
        'color': MENU_COLORS.pool_blue,
        'position':  ((SCREEN_WIDTH // 2) + 15, 40)
    },
    {
        'color': MENU_COLORS.pink,
        'position':  ((SCREEN_WIDTH // 2) + 25, 30)
    },
)


def switch_title(font: Font, color: tuple, position=None):
    font.alter_font_color(color)

    if position:
        font.set_font_location_by_mid(mid=position[0], top=position[1])

    return font


def print_game_title(screen_frame: int, title_font: Font):
    for blink in range(0, screen_frame):
        font = switch_title(
            title_font,
            CURSOR_BLINK_CONFIG[blink]['color'],
            CURSOR_BLINK_CONFIG[blink]['position']
        )
        font.print_font(SCREEN)


def menu():
    pygame.mixer.music.load(str(INTRO_MUSIC))
    pygame.mixer.music.set_volume(GAME_VOLUME)
    pygame.mixer.music.play(-1)

    CLOCK.tick(10)
    direction = UP
    enter = False

    play_font = Font(text='PLAY',
                     style=PIXELED_FONT,
                     size=15,
                     position=PLAY_FONT_POSITION)

    quit_font = Font(text='QUIT',
                     style=PIXELED_FONT,
                     size=15, position=QUIT_FONT_POSITION)

    game_title = Font(text='Snake Game',
                      style=PIXELED_FONT,
                      size=30, position=GAME_TITLE_FONT_POSITION)

    screen_frame = 0

    pointer_colors = (BLACK_RGB, AQUA_RGB)

    best_score = create_best_score_file()

    while True:
        changed_pointer_position = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if should_go_up(event.key):
                    changed_pointer_position = True
                    direction = UP

                if should_go_down(event.key):
                    changed_pointer_position = True
                    direction = DOWN

                if enter_pressed(event.key):
                    enter = True

        SCREEN.fill(MENU_COLORS.black)

        if direction == UP:
            current_play_text_color = MENU_COLORS.pink
            current_quit_color = MENU_COLORS.white

            pointer_position = ((SCREEN_WIDTH // 2) - 45, 183)

            if enter:
                pygame.mixer.music.stop()
                pygame.time.wait(50)
                HIT_ENTER_SOUND.play()

                SCREEN.fill(GARDEN_SCREEN_COLOR)
                pygame.display.update()

                best_score = play_game(best_score)

                enter = False
                pygame.mixer.music.load(str(INTRO_MUSIC))
                pygame.mixer.music.play(-1)
                continue

        elif direction == DOWN:
            current_play_text_color = MENU_COLORS.white
            current_quit_color = MENU_COLORS.pink

            pointer_position = ((SCREEN_WIDTH // 2) - 45, 213)

            if enter:
                HIT_ENTER_SOUND.play()
                pygame.time.wait(100)
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        pygame.draw.circle(
            surface=SCREEN,
            color=pointer_colors[screen_frame % 2],
            center=pointer_position,
            radius=4
        )

        if screen_frame > 0:
            print_game_title(screen_frame, game_title)

        play_font.alter_font_color(current_play_text_color)
        play_font.print_font(SCREEN)

        quit_font.alter_font_color(current_quit_color)
        quit_font.print_font(SCREEN)

        if not changed_pointer_position:
            pygame.time.wait(300)

        pygame.display.update()

        screen_frame = (screen_frame + 1) % 4


if __name__ == '__main__':
    menu()
