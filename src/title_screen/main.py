import pygame
import time

from game_settings.index import game_settings as gs
from graphic_motor.index import update_graphics
from graphic_motor.graphic_items import Basic_item
from title_screen.title_button import Title_button

def run_title(screen) :
    title_done = False
    width = gs["display"].window_width
    height = gs["display"].window_height

    background = Basic_item(pygame.Surface((width, height)))
    background.surface.fill(gs["color"].pale_dark_blue)

    title = Basic_item(pygame.Surface((width * 0.8, height * 0.4)), [width * 0.1, height * 0.3])
    title.surface.fill(gs["color"].grey)

    button1 = Title_button(gs["color"].grey)
    button1.position = [width * 0.4, height * 0.7]
    button2 = Title_button(gs["color"].red)
    button2.position = [width * 0.07, height * 0.7]
    button3 = Title_button(gs["color"].yellow)
    button3.position = [width * 0.73, height * 0.7]
    buttons = [button1, button2, button3]
    
    initTime = time.time()

    while not title_done:
        deltaTime = time.time() - initTime

        ## Handle player's commands
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_done = True
        
        ## Change game state
        
        if deltaTime > 1 and deltaTime <= 1.8:
            title.speed = [0, -2]
        else:
            title.speed = [0, 0]

        if deltaTime > 1.3 and deltaTime <= 1.8:
            for button in buttons:
                button.make_visible(deltaTime)

        ## Update graphics
        items = [[background], buttons + [title]]
        for layer in items:
            for item in layer:
                item.update()
        update_graphics(screen, items)
        pygame.time.delay(int(1000/60))
    
    return 0, True