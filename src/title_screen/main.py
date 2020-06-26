import pygame
import time

from game_settings.index import game_settings as gs
import sound_manager.index as sound
from graphic_motor.index import update_graphics
from graphic_motor.graphic_items import Basic_item
from title_screen.classes import Title, Title_button

window_width = gs["display"].window_width
button_width = gs["title_screen"].button_width
buttons_speed = gs["title_screen"].buttons_speed
buttons_displayed = gs["title_screen"].buttons_displayed

def generate_button_list(props_list, target, has_apeared):
    buttons_number = len(props_list)
    buttons_list = []
    for i in range(1 - buttons_displayed, buttons_displayed):
        button_position = [(window_width - button_width) / 2 + i * (button_width + gs["title_screen"].buttons_spacing), gs["title_screen"].buttons_top]
        buttons_list.append(Title_button(props_list[(target + i) % buttons_number], button_position, has_apeared))
    return buttons_list

def run_title(screen) :
    ## Variables for the loop
    title_done = False
    next_state = 0
    exit_game = False
    is_starting = True
    waiting_commands = False
    time_stamp = time.time()
    button_target = 0

    ## Elements
    background = Basic_item(pygame.Surface((window_width, gs["display"].window_height)), [0, 0], [0, 0])
    background.surface.fill(gs["color"].pale_dark_blue)

    title = Title()

    button1 = {"label": "Button 1", "color": gs["color"].grey, "effect": lambda : (False, 0, False)}
    button2 = {"label": "Button 2", "color": gs["color"].red, "effect": lambda : (False, 0, False)}
    button3 = {"label": "Reset", "color": gs["color"].yellow, "effect": lambda : (True, run_title, False)}
    button4 = {"label": "Exit", "color": gs["color"].purple, "effect": lambda : (True, 0, True)}
    buttons_props = [button1, button2, button3, button4]

    buttons = generate_button_list(buttons_props, button_target, False)

    left_key = False
    right_key = False
    space_key = False

    sound.init_music("sample_music.mp3")

    while not title_done:
        ## Register player's commands
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0, True
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_key = (event.type == pygame.KEYDOWN)
                if event.key == pygame.K_RIGHT:
                    right_key = (event.type == pygame.KEYDOWN)
                if event.key == pygame.K_SPACE:
                    space_key = (event.type == pygame.KEYDOWN)

        ## Update game
        if is_starting:
            if time.time() - time_stamp > gs["title_screen"].time_end_intro:
                is_starting = False
                waiting_commands = True
        else:
            if not waiting_commands:
                if time.time() - time_stamp > gs["title_screen"].time_move:
                    for button in buttons:
                        button.speed[0] = 0
                    buttons = generate_button_list(buttons_props, button_target, True)
                    waiting_commands = True
            else:
                if space_key:
                    sound.noise_library["noise_sample"].play()
                    title_done, next_state, exit_game = buttons[buttons_displayed - 1].effect()
                elif left_key:
                    sound.noise_library["noise_sample"].play()
                    waiting_commands = False
                    time_stamp = time.time()
                    button_target = (button_target - 1) % len(buttons_props)
                    for button in buttons:
                        button.time_stamp = time_stamp
                        button.speed[0] = buttons_speed
                elif right_key:
                    sound.noise_library["noise_sample"].play()
                    waiting_commands = False
                    time_stamp = time.time()
                    button_target = (button_target + 1) % len(buttons_props)
                    for button in buttons:
                        button.time_stamp = time_stamp
                        button.speed[0] = - buttons_speed
        
        ## Update graphics
        items = [[background], buttons + [title]]
        for layer in items:
            for item in layer:
                item.update()
        update_graphics(screen, items)
        pygame.time.delay(round(1000/gs["display"].fps))
    
    sound.stop_music()
    background.surface.fill(gs["color"].black)
    update_graphics(screen, [[background]])
    return next_state, exit_game