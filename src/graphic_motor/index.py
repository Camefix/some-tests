import pygame

def update_graphics (screen, items):
    for layer in items:
        for item in layer:
            screen.blit(item.surface, item.position)
    pygame.display.update()