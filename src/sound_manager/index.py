import pygame
import os

noise_library = {}

def init_noise_library():
    noise_references = os.listdir("Audio//Noises")
    for noise in noise_references:
        noise_name = noise.replace(".wav", "")
        noise_address = "Audio//Noises//" + noise
        noise_library[noise_name] = pygame.mixer.Sound(noise_address)

def init_music(music):
    pygame.mixer.music.load("Audio//Musics//" + music)
    pygame.time.delay(200)
    pygame.mixer.music.play(loops = -1)

def stop_music():
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.stop()


def change_music(music):
    stop_music()
    init_music(music)

