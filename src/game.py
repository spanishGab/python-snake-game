import sys
import pygame
from pygame.locals import QUIT, KEYDOWN

from .constants import (
    UP, DOWN, LEFT, RIGHT, CLOCK, GAME_SOUNDS_DIR, GAME_VOLUME, SCREEN,
    SCREEN_HEIGHT, SCREEN_WIDTH, GARDEN_SCREEN_COLOR, FREE_SANS_BOLD_FONT,
    PIXELED_FONT
)
from .entities.Font import Font
from .entities.Apple import Apple
from .entities.Snake import Snake
from .db import update_best_score
from .utils.keyboard import (should_go_up, should_go_down, should_go_left,
                             should_go_right)

pygame.display.set_caption('Snake')

SCORE_TEXT_POSITION = (SCREEN_WIDTH - 110, 10)

BEST_SCORE_TEXT_POSITION = (120, 10)

GAME_OVER_TEXT_POSITION = (SCREEN_WIDTH // 2, 20)

GAME_OVER_TEXT_COLOR = (255, 26, 26)

GAME_OVER_SOUND = pygame.mixer.Sound(
    str(GAME_SOUNDS_DIR.joinpath('game-over.ogg'))
)
GAME_OVER_SOUND.set_volume(GAME_VOLUME)

EAT_CARROT_SOUND = pygame.mixer.Sound(
    str(GAME_SOUNDS_DIR.joinpath('carrot.ogg'))
)
EAT_CARROT_SOUND.set_volume(GAME_VOLUME)

HAPPY_CAVE_MUSIC = GAME_SOUNDS_DIR.joinpath('happy-cave.ogg')


def collision(x: tuple, y: tuple):
    return (x[0] == y[0]) and (x[1] == y[1])


def play_game(best_score: int):
    pygame.time.wait(200)
    pygame.mixer.music.load(str(HAPPY_CAVE_MUSIC))
    pygame.mixer.music.play(-1)

    snake = Snake(
        head_initial_position=(200, 200),
        middle_initial_position=(210, 200),
        tail_initial_position=(220, 200),
        head_color=(255, 102, 0),
        body_color=(255, 153, 3)
    )

    apple = Apple()

    current_direction = LEFT
    score = 0

    score_font = Font(text='Score: {score}',
                      style=FREE_SANS_BOLD_FONT,
                      size=22,
                      position=SCORE_TEXT_POSITION)

    best_score_font = Font(text=f'Best-Score: {best_score}',
                           style=FREE_SANS_BOLD_FONT,
                           size=22,
                           position=BEST_SCORE_TEXT_POSITION)

    while True:
        CLOCK.tick(snake.speed)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if should_go_up(event.key) and current_direction != DOWN:
                    current_direction = UP
                    break

                elif should_go_down(event.key) and current_direction != UP:
                    current_direction = DOWN
                    break

                elif should_go_left(event.key) and current_direction != RIGHT:
                    current_direction = LEFT
                    break

                elif should_go_right(event.key) and current_direction != LEFT:
                    current_direction = RIGHT
                    break

        # did the snake ate an apple?
        if collision(snake.body[0], apple.apple_position):
            pygame.mixer.Sound.play(EAT_CARROT_SOUND)
            apple.generate_new_random_apple_position()
            snake.increase_size()
            score += 1

        snake.update_location(current_direction)

        # has snake colided with itself?
        for snake_part in snake.body[1:]:
            if collision(snake.body[0], snake_part):
                snake.is_alive = False
                break

        # has snake reached the screen edge?
        if (
            snake.body[0][0] in (0, SCREEN_WIDTH)
            or snake.body[0][1] in (0, SCREEN_HEIGHT)
        ):
            snake.is_alive = False

        SCREEN.fill(GARDEN_SCREEN_COLOR)

        pygame.draw.circle(
            surface=SCREEN,
            color=apple.color,
            center=(apple.apple_position[0] + 5, apple.apple_position[1] + 5),
            radius=5
        )

        score_font.alter_font_text(f'Score: {score}')
        print(score)
        score_font.print_font(SCREEN)

        best_score_font.print_font(SCREEN)

        snake.print_snake(SCREEN)

        if not snake.is_alive:
            if score > best_score:
                update_best_score(score)

            pygame.mixer.music.stop()
            break

        pygame.display.update()

    Font(text="Game Over",
         style=PIXELED_FONT,
         size=50,
         position=GAME_OVER_TEXT_POSITION,
         color=GAME_OVER_TEXT_COLOR).print_font(SCREEN)

    pygame.display.update()

    pygame.mixer.Sound.play(GAME_OVER_SOUND)

    pygame.time.wait(2000)
