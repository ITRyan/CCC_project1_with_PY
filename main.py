import pygame
from fighter import Fighter
pygame.init()  # initialize pi game

# create game window
SCREEN_WIDTH = 1000 
SCREEN_HEIGHT = 600

# this function will create a game window for us . two initial arguments screen_width & screen_height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighter")  # The tittle of the game

# set framerate
clock = pygame.time.Clock()
FPS = 60

# next add a game loop,it will allow the game to continuously run take actions draw the players and etc until I actually choose to exit
# setting up the loop baseed on that variable ~GAME LOOP~

# define colours
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# define fighter variables
AKAZA_SIZE_W = 413
AKAZA_SIZE_H = 989
AKAZA_SCALE = 0.25
AKAZA_OFFSET=[0,0]
AKAZA_DATA = [AKAZA_SIZE_W,AKAZA_SIZE_H]
# AKAZA_DATA = [AKAZA_SIZE_W,AKAZA_SIZE_H,AKAZA_SCALE,AKAZA_OFFSET]

#load background image before the game
bg_image = pygame.image.load(
    "assets/images/background.jpg").convert_alpha() #Once an image has been converted it can be blitted (drawn) onto another surface

# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0)) # The blit() method is then used to draw the background image onto the screen at position(0,0)


# create two instances of fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)


# game loop
run = True
while run: #while run is True execute all the code below this

    clock.tick(FPS)

    # draw background
    draw_bg()

 
    # move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)

    # #update fighters
    # fighter_1.update()
    # fighter_2.update()
    
    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    #When you click on the x in the top corner of the screen or the window i want to kicked out of this while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # update display
    pygame.display.update()

# exit pygame
pygame.quit()
