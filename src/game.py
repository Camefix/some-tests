import pygame
import game_settings.display as display
from title_screen.main import run_title

def run_game():
    game_done = False
    actual_gameplay = run_title

    pygame.init()
    screen = pygame.display.set_mode((display.window_width, display.window_height))
    pygame.display.set_caption("Tests")

    while not game_done:
        actual_gameplay, game_done = actual_gameplay(screen)

    pygame.display.quit()
    pygame.quit()