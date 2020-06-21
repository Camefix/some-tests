import pygame
import src.game_settings.index as gs


def run_game():
    done = False
    pygame.init()
    screen = pygame.display.set_mode((gs.display.window_width, gs.display.window_height))
    pygame.display.set_caption("Tests")


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        
        pygame.time.delay(60)


    pygame.display.quit()
    pygame.quit()