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
AKAZA_SIZE = 288
AKAZA_SCALE = 1
AKAZA_OFFSET=[72,56]
AKAZA_DATA = [AKAZA_SIZE,AKAZA_SCALE,AKAZA_OFFSET]

#load background image before the game
bg_image = pygame.image.load(
    "assets/images/Background_Kimetsu_No_Yaiba.jpg").convert_alpha() #Once an image has been converted it can be blitted (drawn) onto another surface

# load spritesheets
akaza_sheet = pygame.image.load(
    "assets/images/Akaza/AKAZA_SHEET.png").convert_alpha()

# define number of steps in each animation
AKAZA_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]

# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(bg_image, (0, 0)) # The blit() method is then used to draw the background image onto the screen at position(0,0)

# function for drawing fighter health bars


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-2, y-2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400*ratio, 30))


# create two instances of fighters
fighter_1 = Fighter(200, 310, False,AKAZA_DATA,akaza_sheet, AKAZA_ANIMATION_STEPS)
fighter_2 = Fighter(700, 310,True ,AKAZA_DATA,akaza_sheet, AKAZA_ANIMATION_STEPS)


# game loop
run = True
while run: #while run is True execute all the code below this

    clock.tick(FPS)

    # draw background
    draw_bg()

  # show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    # move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)

    #update fighters
    fighter_1.update()
    fighter_2.update()
    
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
