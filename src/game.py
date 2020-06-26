import pygame


def run_game():
    pygame.mixer.pre_init(buffer=256)
    pygame.init()
    from game_settings.index import game_settings as gs
    from title_screen.main import run_title
    from sound_manager.index import init_noise_library, noise_library

    game_done = False
    actual_gameplay = run_title
    screen = pygame.display.set_mode((gs["display"].window_width, gs["display"].window_height))
    pygame.display.set_caption("Tests")
    init_noise_library()

    while not game_done:
        actual_gameplay, game_done = actual_gameplay(screen)

    pygame.display.quit()
    pygame.quit()