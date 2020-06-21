import pygame
import gameSettings.display as ds

print("Ok")
WIDTH = 500
HEIGHT = 500
size = (WIDTH, HEIGHT)
done = False
'''

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tests")


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Attendre un peu pour reboucler (10 pour 1/10 seconde).
    pygame.time.delay(60)

#Pour fermer la fenêtre si l'on clique sur le bouton, très important.
pygame.display.quit()
pygame.quit()
'''