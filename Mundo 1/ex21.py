#reproduzindo um MP3

import pygame, time

pygame.mixer.init()

pygame.mixer_music.load('Luto Theo.mp3')

pygame.mixer_music.play()

time.sleep(1)

pygame.mixer_music.stop()



