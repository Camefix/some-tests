import pygame
from game_settings.index import game_settings as gs

from graphic_motor.index import update_graphics
from graphic_motor.graphic_items import basic_item

def run_title(screen) :
    title_done = False
    width = gs["display"].window_width
    height = gs["display"].window_height

    background = basic_item(pygame.Surface((width, height)))
    background.surface.fill(gs["color"].pale_dark_blue)

    title = basic_item(pygame.Surface((width * 0.8, height * 0.4)), (width * 0.1, height * 0.3))
    title.surface.fill(gs["color"].grey)
    
    while not title_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_done = True
        
        items = [[background], [title]]
        update_graphics(screen, items)
        pygame.time.delay(60)
    
    return 0, True