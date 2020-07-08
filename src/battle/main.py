import pygame
import time

from game_settings.index import game_settings as gs
import sound_manager.index as sound
from graphic_motor.index import update_graphics
from graphic_motor.graphic_items import Basic_item
from battle.classes import *


def run_battle(screen, props) :
    ## Variables for the loop
    battle_done = False
    next_state = 0
    exit_game = False

    ## Elements
    battle_map = Map(props["map"])


    left_key = False
    right_key = False
    up_key = False
    down_key = False
    space_key = False

    while not battle_done:
        ## Register player's commands
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0, True
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_key = (event.type == pygame.KEYDOWN)
                if event.key == pygame.K_RIGHT:
                    right_key = (event.type == pygame.KEYDOWN)
                if event.key == pygame.K_UP:
                    up_key = (event.type == pygame.KEYDOWN)
                if event.key == pygame.K_DOWN:
                    down_key = (event.type == pygame.KEYDOWN)
                if event.key == pygame.K_SPACE:
                    space_key = (event.type == pygame.KEYDOWN)

        ## Update game
        if up_key:
            battle_map.cursor.grid_position[0] -= 1
        elif down_key:
            battle_map.cursor.grid_position[0] += 1
        elif left_key:
            battle_map.cursor.grid_position[1] -= 1
        elif right_key:
            battle_map.cursor.grid_position[1] += 1

        ## Update graphics
        items = [[battle_map]]
        for layer in items:
            for item in layer:
                item.update()
        update_graphics(screen, items)
        pygame.time.delay(round(1000/gs["display"].fps))
    
    sound.stop_music()
    background.surface.fill(gs["color"].black)
    update_graphics(screen, [[background]])
    return next_state, exit_game