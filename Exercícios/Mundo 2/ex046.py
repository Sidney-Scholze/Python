from time import sleep
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('fogos.mp3')



for c in range(10, 0 , -1 ):

    print(c)
    sleep(1)


print('Fogos !!!')
pygame.mixer.music.play()
pygame.event.wait()

