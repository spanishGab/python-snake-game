import os
import pygame
from pygame.locals import *
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_RETURN, K_KP_ENTER

from collections import namedtuple

from src.main_game import play_game
from src.entities.Font import Font



from src.constants.constants import (UP, DOWN, LEFT, RIGHT, CLOCK,
                                      GAME_SOUNDS_DIR, GAME_SCORE_DIR, BEST_SCORE_FILE,
                                      HAPPY_CAVE_MUSIC_SOUND, CARROT_SOUND, GAME_OVER_SOUND,
                                      ENTER_SOUND, INTRO_MUSIC_SOUND, SCREEN, SCREEN_HEIGHT, 
                                      SCREEN_WIDTH, GARDEN_SCREEN_COLOR, FREE_SANS_BOLD_FONT, 
                                      PIXELED_FONT)

PLAY_FONT_POSITION = ((600 // 2), 160)
QUIT_FONT_POSITION = ((600 // 2), 190)
GAME_TITLE_FONT_POSITION = (((600 // 2)-5)+10, 50)

BLACK_RGB = (0, 0, 0)
WHITE_RGB = (255, 255, 255)
POOL_BLUE_RGB = (0, 204, 204)
PINK_RGB = (204, 0, 102)
AQUA_RGB = (0, 255, 255)

Colors = namedtuple("Colors", ['black',
                               'white',
                               'pool_blue',
                               'pink',
                               'aqua'
                               ])


def switch_title(font: Font, color: tuple, position=None):
    font.alter_font_color(color)

    if position:
        font.set_font_location_by_mid(mid=position[0], top=position[1])

    return font


def print_game_title(screen_frame, title_font, colors):
    blink_details = (
        None, 
        {
            'color': colors.white, 
            'position':  (2960, 50)
        }, 
        {
            'color': colors.pool_blue, 
            'position':  (2970, 580)
        },
        {
            'color': colors.pink, 
            'position':  (2980, 570)
        },
    )

    for blink in range(1, screen_frame+1):
        font = switch_title(
            title_font, 
            blink_details[blink]['color'], 
            blink_details[blink]['position']
        )
        font.print_font(SCREEN)


def menu():
    pygame.mixer.music.load(os.path.join(GAME_SOUNDS_DIR, INTRO_MUSIC_SOUND))
    pygame.mixer.music.play(-1)

    CLOCK.tick(10)
    direction = UP
    enter = False
    
    play_font = Font(text='PLAY', 
                     style=PIXELED_FONT, 
                     size=15, position=PLAY_FONT_POSITION)

    quit_font = Font(text='QUIT',
                     style=PIXELED_FONT,
                     size=15, position=QUIT_FONT_POSITION)

    game_title = Font(text='Snake Game',
                      style=PIXELED_FONT, 
                      size=30, position=GAME_TITLE_FONT_POSITION)

    screen_frame = 0
    
    #colors = (((0,0,0), (255, 255, 255), (0, 204, 204), (204, 0, 102)), ((0, 255, 255), (0,0,0)))
    colors = Colors(
        black=BLACK_RGB, 
        white=WHITE_RGB, 
        pool_blue=POOL_BLUE_RGB, 
        pink=PINK_RGB, 
        aqua=AQUA_RGB
    )
    
    pointer_colors = (BLACK_RGB, AQUA_RGB)

    with open(os.path.join(GAME_SCORE_DIR, BEST_SCORE_FILE), mode='r') as r:
        try:
            best_score = int(r.readline())
        except ValueError:
            best_score = 0
    
    while True:
        changed = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    changed = True
                    direction = UP
                if event.key == K_DOWN:
                    changed = True
                    direction = DOWN
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    enter = True
        
        SCREEN.fill(colors.black)

        if direction == UP:
            current_play_text_color = colors.pink
            current_quit_color = colors.white
            
            pointer_position = (255, 183)
            
            if enter:
                pygame.mixer.music.stop()
                pygame.time.wait(50)
                pygame.mixer.Sound.play(
                    pygame.mixer.Sound(os.path.join(GAME_SOUNDS_DIR, ENTER_SOUND))
                )

                SCREEN.fill(GARDEN_SCREEN_COLOR)
                pygame.display.update()

                play_game(best_score)

                enter = False
                pygame.mixer.music.load(os.path.join(GAME_SOUNDS_DIR, 
                                                     INTRO_MUSIC_SOUND))
                pygame.mixer.music.play(-1)
                continue

        elif direction == DOWN:
            current_play_text_color = colors.white
            current_quit_color = colors.pink

            pointer_position = (255, 213)

            if enter:
                pygame.mixer.Sound.play(
                    pygame.mixer.Sound(os.path.join(GAME_SOUNDS_DIR, ENTER_SOUND))
                )
                pygame.time.wait(100)
                pygame.display.quit()
                pygame.quit()
                exit()
                
        pygame.draw.circle(SCREEN, pointer_colors[screen_frame%2], pointer_position, 4)

        if screen_frame > 0:
            print_game_title(screen_frame, game_title, colors)

        play_font.alter_font_color(current_play_text_color)
        play_font.print_font(SCREEN)

        quit_font.alter_font_color(current_quit_color)
        quit_font.print_font(SCREEN)

        if not changed:
            pygame.time.wait(300)
            
        pygame.display.update()

        screen_frame = (screen_frame + 1) % 4

if __name__ == '__main__':
    menu()