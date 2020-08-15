import pygame as pyg
from pygame.locals import *
import os
dir_name = os.path.join(os.path.dirname(__file__))

from main_game import play_game
from GameConfig.config import *
from GameConfig.Fonts import Fonts


def print_game_title(i, screen, title_font, colors):
    if i == 1:
        font = switch_title(title_font, colors[0][i], ((295+i*10), 50))
        font.print_font(screen)
    elif i == 2:
        font = switch_title(title_font, colors[0][i-1], ((295+(i-1)*10), 50))
        font.print_font(screen)
        font = switch_title(title_font, colors[0][i], ((295+i*10), (60-i*10)))
        font.print_font(screen)
    elif i == 3:
        font = switch_title(title_font, colors[0][i-2], (((295+(i-2)*10), 50)))
        font.print_font(screen)
        switch_title(title_font, colors[0][i-1], ((295+(i-1)*10), (60-(i-1)*10)))
        font.print_font(screen)
        switch_title(title_font, colors[0][i], ((295+i*10), (60-i*10)))
        font.print_font(screen)


def menu():
    pyg.mixer.music.load('GameSounds/intro-music.ogg')
    pyg.mixer.music.play(-1)

    clock.tick(10)
    direction = UP
    enter = False
    
    play_font = Fonts('PLAY', 'Pixeled.ttf', 15, ((600 // 2), 160))
    quit_font = Fonts('QUIT', 'Pixeled.ttf', 15, ((600 // 2), 190))
    title_font = Fonts('Snake Game', 'Pixeled.ttf', 30, (((600 // 2)-5)+10, 50))
    i = 0
    
    colors = (((0,0,0), (255, 255, 255), (0, 204, 204), (204, 0, 102)), ((0, 255, 255), (0,0,0)))

    with open(os.path.join(dir_name, 'best_score.txt'), 'r') as r:
        try:
            best_score = int(r.readline())
        except ValueError:
            best_score = 0
    
    while True:
        changed = False
        for event in pyg.event.get():
            if event.type == QUIT:
                pyg.display.quit()
                pyg.quit()
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
        
        screen.fill(colors[0][0])

        if direction == UP:
            current_play_color = colors[0][3]
            current_quit_color = colors[0][1]
            pointer_direction = (255, 183)
            if enter:
                pyg.mixer.music.stop()
                pyg.time.wait(50)
                pyg.mixer.Sound.play(pyg.mixer.Sound("GameSounds/enter.ogg"))
                screen.fill((51, 204, 51))
                pyg.display.update()

                play_game(best_score)

                enter = False
                pyg.mixer.music.load('GameSounds/intro-music.ogg')
                pyg.mixer.music.play(-1)
                continue

        elif direction == DOWN:
            current_play_color = colors[0][1]
            current_quit_color = colors[0][3]
            pointer_direction = (255, 213)
            if enter:
                pyg.mixer.Sound.play(pyg.mixer.Sound("GameSounds/enter.ogg"))
                pyg.time.wait(100)
                pyg.display.quit()
                pyg.quit()
                exit()
                
        pyg.draw.circle(screen, colors[1][i%2], pointer_direction, 4)

        if i > 0:
            print_game_title(i, screen, title_font, colors)

        play_font.alter_color(current_play_color)
        play_font.print_font(screen)

        quit_font.alter_color(current_quit_color)
        quit_font.print_font(screen)

        if not changed:
            pyg.time.wait(300)
            
        pyg.display.update()

        i = (i + 1) % 4

if __name__ == '__main__':
    menu()