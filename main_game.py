import os
dir_name = os.path.join(os.path.dirname(__file__))

import pygame
import random
from pygame.locals import *

from Snake import Snake
from Apple import Apple
from GameConfig.config import *

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2)
pygame.mixer.init()
pygame.display.set_caption('Snake')


def make_game(best_score):
    pygame.mixer.music.load('GameSounds/happy-cave.ogg')
    pygame.mixer.music.play(-1)  # TODO Make the music stop when game ends

    snake = Snake(head=(200, 200), mid=(210, 200), tail=(220,200), head_color=(255, 102, 0), body_color=(255, 153, 3))

    apple = Apple()

    my_direction = LEFT
    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0
    dead_line = False

    while True:
        clock.tick(snake.get_speed())
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_KP8) and my_direction != DOWN:
                    my_direction = UP
                    break
                elif (event.key == K_DOWN or event.key == K_KP2) and my_direction != UP:
                    my_direction = DOWN
                    break
                elif (event.key == K_LEFT or event.key == K_KP4) and my_direction != RIGHT:
                    my_direction = LEFT
                    break
                elif (event.key == K_RIGHT or event.key == K_KP6) and my_direction != LEFT:
                    my_direction = RIGHT
                    break

        if collision(snake.get_snake()[0], apple.get_apple_pos()):
            pygame.mixer.Sound.play(pygame.mixer.Sound("GameSounds/carrot.ogg"))
            apple.create()
            snake.increase_size()
            score += 1

        snake.update_location(my_direction)

        snake_head = snake.get_snake()[0]
        if list(filter(lambda part: collision(snake_head, part), snake.get_snake()[1:])):
            dead_line = True
        
        if ((snake_head[0] == 600 or snake_head[1] == 600) or (snake_head[0] == 0 or snake_head[1] == 0)):
            dead_line = True

        screen.fill((51, 204, 51))
        screen.blit(apple.get_apple(), apple.get_apple_pos())
        # pygame.draw.circle(screen, apple.get_color(), apple.get_apple_pos(), 5)  #TODO: apple circle

        score_font = font.render(f'Score: {score}', True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (600 - 120, 10)
        screen.blit(score_font, score_rect)

        b_score_font = font.render(f'Best-Score: {best_score}', True, (255, 255, 255))
        b_score_rect = b_score_font.get_rect()
        b_score_rect.topleft = (40, 10)
        screen.blit(b_score_font, b_score_rect)

        snake.print_snake(screen)
        
        if dead_line:
            if score > best_score:
                with open(os.path.join(dir_name, 'best_score.txt'), 'w') as r:
                    r.write(str(score))
            break

        pygame.display.update()

    while True:
        game_over_font = pygame.font.Font('freesansbold.ttf', 50)
        game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
        game_over_rect = game_over_screen.get_rect()
        game_over_rect.midtop = (600 // 2, 20)
        screen.blit(game_over_screen, game_over_rect)
        pygame.display.update()
        pygame.time.wait(60)
        draw_menu()


def draw_menu():
    clock.tick(10)
    direction = UP
    enter = False
    
    play_font = create_font('PLAY', 'Pixeled', 15, ((600 // 2), 160))
    quit_font = create_font('QUIT', 'Pixeled', 15, ((600 // 2), 190))
    title_font = create_font('Snake Game', 'Pixeled', 30, (((600 // 2)-5)+10, 50))
    i = 0
    
    colors = ((0,0,0), (255, 255, 255), (0, 204, 204), (204, 0, 102))
    pointer_colors = ((0, 255, 255), (0,0,0))

    with open(os.path.join(dir_name, 'best_score.txt'), 'r') as r:
        try:
            best_score = int(r.readline())
        except:
            best_score = -1
    

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
        
        screen.fill(colors[0])

        if direction == UP:
            current_play_color = colors[3]
            current_quit_color = colors[1]
            pointer_direction = (255, 183)
            if enter:
                screen.fill((51, 204, 51))
                pygame.display.update()
                make_game(best_score)
                pygame.time.wait(7000)
                break

        elif direction == DOWN:
            current_play_color = colors[1]
            current_quit_color = colors[3]
            pointer_direction = (255, 213)
            if enter:
                pygame.display.quit()
                pygame.quit()
                exit()
                
        pygame.draw.circle(screen, pointer_colors[i%2], pointer_direction, 4)

        if i == 0: # TODO: verify the pattern to simplify this code
            pass
        elif i == 1:
            font = switch_title(title_font, colors[i], (((600 // 2)-5)+10, 50))
            font.print_font(screen)
        elif i == 2:
            font = switch_title(title_font, colors[i-1], (((600 // 2)-5)+10, 50))
            font.print_font(screen)
            font = switch_title(title_font, colors[i], ((600 // 2)- 5 + (i*10), 60 - (i*10)))
            font.print_font(screen)
        elif i == 3:
            switch_title(title_font, colors[i-2], (((600 // 2)-5)+10, 50))
            font.print_font(screen)
            switch_title(title_font, colors[i-1], ((600 // 2)- 5 + ((i-1)*10), 60 - ((i-1)*10)))
            font.print_font(screen)
            switch_title(title_font, colors[i], ((600 // 2)- 5 + (i*10), 60 - (i*10)))
            font.print_font(screen)
            

        alter_font_color(play_font, current_play_color)
        play_font.print_font(screen)

        alter_font_color(quit_font, current_quit_color)
        quit_font.print_font(screen)

        if not changed:
            pygame.time.wait(300)
            
        pygame.display.update()

        i = (i + 1) % 4
        

draw_menu()

