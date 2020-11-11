# Faça um programa em python que abra e use um audio em arquivo mp3
# Dessa forma abre o groove musicas
'''import os, time
os.startfile(r'shoottothrill.mp3')
time.sleep(10)'''

# Dessa forma toca pelo próprio python
import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('shoottothrill.mp3')
pygame.mixer.music.play()
pygame.event.wait()