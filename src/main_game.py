import os
dir_name = os.path.join(os.path.dirname(__file__))

import pygame
from pygame.locals import (QUIT, KEYDOWN, 
                           K_UP, K_DOWN, K_LEFT, K_RIGHT,
                           K_KP8, K_KP2, K_KP4, K_KP6,
                           K_e, K_d, K_s, K_f)


from .entities.Snake import Snake
from .entities.Apple import Apple
from .entities.Font import Font

from .constants.constants import (UP, DOWN, LEFT, RIGHT, CLOCK,
                                  GAME_SOUNDS_DIR, GAME_SCORE_DIR, BEST_SCORE_FILE,
                                  HAPPY_CAVE_MUSIC_SOUND, CARROT_SOUND, GAME_OVER_SOUND,
                                  SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, GARDEN_SCREEN_COLOR,
                                  FREE_SANS_BOLD_FONT, PIXELED_FONT)

from.utils import utils

pygame.display.set_caption('Snake')


SCORE_TEXT_POSITION = (SCREEN_WIDTH - 110, 10)
BEST_SCORE_TEXT_POSITION = (120, 10)
GAME_OVER_TEXT_POSITION = (SCREEN_WIDTH // 2, 20)
GAME_OVER_TEXT_COLOR = (255, 26, 26)


def play_game(best_score):
    pygame.time.wait(200)
    pygame.mixer.music.load(os.path.join(GAME_SOUNDS_DIR, HAPPY_CAVE_MUSIC_SOUND))
    pygame.mixer.music.play(-1)

    snake = Snake(
        head_initial_position=(200, 200),
        middle_initial_position=(210, 200),
        tail_initial_position=(220,200), 
        head_color=(255, 102, 0),
        body_color=(255, 153, 3)
    )

    apple = Apple()

    my_direction = LEFT
    score = 0
    snake_died = False

    while True:
        CLOCK.tick(snake.speed)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_KP8 or event.key == K_e):
                    if my_direction != DOWN:
                        
                        my_direction = UP
                        break

                elif (event.key == K_DOWN or event.key == K_KP2 or event.key == K_d):
                    if my_direction != UP:

                        my_direction = DOWN
                        break

                elif (event.key == K_LEFT or event.key == K_KP4 or event.key == K_s):
                    if my_direction != RIGHT:
                    
                        my_direction = LEFT
                        break

                elif (event.key == K_RIGHT or event.key == K_KP6 or event.key == K_f):
                    if my_direction != LEFT:

                        my_direction = RIGHT
                        break

        if utils.collision(snake.snake[0], apple.apple_position):
            pygame.mixer.Sound.play(
                pygame.mixer.Sound(os.path.join(GAME_SOUNDS_DIR, CARROT_SOUND))
            )
            apple.generate_new_random_apple_position()
            snake.increase_size()
            score += 1

        snake.update_location(my_direction)

        if list(filter(lambda part: utils.collision(snake.snake[0], part), 
                       snake.snake[1:])):
            snake_died = True
        
        if (snake.snake[0][0] in (0, SCREEN_WIDTH) or 
            snake.snake[0][1] in (0, SCREEN_HEIGHT)):
            snake_died = True

        SCREEN.fill(GARDEN_SCREEN_COLOR)

        pygame.draw.circle(
            SCREEN, apple.color, 
            (apple.apple_position[0]+5, apple.apple_position[1]+5), 5
        )

        score_font = Font(text=f'Score: {score}',
                           style=FREE_SANS_BOLD_FONT,
                           size=22, position=SCORE_TEXT_POSITION)
        score_font.print_font(SCREEN)

        best_score_font = Font(text=f'Best-Score: {best_score}',
                                style=FREE_SANS_BOLD_FONT,
                                size=22, position=BEST_SCORE_TEXT_POSITION)
        best_score_font.print_font(SCREEN)
        
        snake.print_snake(SCREEN)
        
        if snake_died:
            if score > best_score:
                with open(os.path.join(GAME_SCORE_DIR, BEST_SCORE_FILE), mode='w') as r:
                    r.write(str(score))
            pygame.mixer.music.stop()
            break

        pygame.display.update()

    
    game_over = Font(text="Game Over", 
                      style=PIXELED_FONT, 
                      size=50, position=GAME_OVER_TEXT_POSITION, 
                      color=GAME_OVER_TEXT_COLOR)
    game_over.print_font(SCREEN)
    
    pygame.display.update()
    
    pygame.mixer.Sound.play(
        pygame.mixer.Sound(os.path.join(GAME_SOUNDS_DIR, GAME_OVER_SOUND))
    )
    pygame.time.wait(2000)
