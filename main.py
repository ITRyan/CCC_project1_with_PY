import pygame
from fighter import Fighter
import os
import random
import math
from os import listdir
from os.path import isfile, join
pygame.init()  # initialize py game

pygame.display.set_caption("Fighter")  # The tittle of the game

# define colours for background
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# set framerate
clock = pygame.time.Clock()
FPS = 60
PLAYER_VEL=5

# create game window
WIDTH,HEIGHT = 1000 ,600
# this function will create a game window for us . two initial arguments screen_width & screen_height
window = pygame.display.set_mode((WIDTH,HEIGHT))

#load background image
bg_image = pygame.image.load("assets/images/background.jpg").convert_alpha()
    


def draw_bg():
   scaled_bg = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
   window.blit(scaled_bg, (0, 0))
    



def main(window):
    clock = pygame.time.Clock()
    #draw background
    draw_bg()
    pygame.display.update()
    run =True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break

    pygame.quit()
    quit()        



if __name__=="__main__":
    main(window)


