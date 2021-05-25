import pygame
import os

from pygame.constants import K_1

pygame.init()
# game constants
# setup display
WIDTH, HEIGHT = 950, 650
# game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# window title
pygame.display.set_caption("Journey to Python")

# setup game loop
# frames per second
FPS = 60

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
INPUT_BOX = pygame.Rect(150, HEIGHT-65, 140, 32)
# game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# boarder between game and code
BOARDER = pygame.Rect(WIDTH//4-2.5, 0, 5, HEIGHT)
INFO_BOARDER = pygame.Rect(0, HEIGHT - 125, WIDTH, HEIGHT)


# load images
HOME_PLANET = pygame.image.load(os.path.join("planet1.svg"))
PLANET_PYTHON = pygame.image.load(os.path.join("planet2.png"))
ROCKET_1_IMAGE = pygame.image.load(os.path.join("rocket1.svg"))
ROCKET_2_IMAGE = pygame.image.load(os.path.join("starting-rocket.svg"))
SPACE_BG_IMAGE = pygame.image.load(os.path.join("milky-way.jpg"))
# rotate and resize images
# resize values
ROCKET_WIDTH = 50
ROCKET_HEIGHT = 75
ROCKET_1 = pygame.transform.rotate(pygame.transform.scale(
    ROCKET_1_IMAGE, (ROCKET_WIDTH, ROCKET_HEIGHT)), 20)
ROCKET_2 = pygame.transform.rotate(pygame.transform.scale(
    ROCKET_2_IMAGE, (ROCKET_WIDTH-10, ROCKET_HEIGHT+10)), -25)
SPACE_BG = pygame.transform.scale(SPACE_BG_IMAGE, (WIDTH, HEIGHT))
# speed of rocket
ROCKET_VEL = 3

# button vars
# gameplay  vars

COLOR_ACTIVE = (0, 0, 255)
COLOR_INACTIVE = (255, 255, 255)


def draw_window(text_surface, col, red, white):
    
    # game window background
    WIN.blit(SPACE_BG, (0, 0))
    # game images
    WIN.blit(HOME_PLANET, (50, 400))
    WIN.blit(PLANET_PYTHON, (600, 50))
    WIN.blit(ROCKET_1, (white.x, white.y))
    WIN.blit(ROCKET_2, (red.x, red.y))
    # make info rect
    pygame.draw.rect(WIN, GRAY, INFO_BOARDER)
    pygame.draw.rect(WIN, col, INPUT_BOX, 2)
    
    WIN.blit(text_surface, (INPUT_BOX.x+5, INPUT_BOX.y+5))
    

def gameplay(key_pressed, white, red):
    # onscreen text
    # user input
    # rocket movement
    if key_pressed[pygame.K_1]:
        white.x += 4
        white.y -= 2
    if key_pressed[pygame.K_2]:
        white.x += 8
        white.y -= 4
    if key_pressed[pygame.K_3]:
        red.x += 4
        red.y -= 2
    if key_pressed[pygame.K_4]:
        red.x += 8
        red.y -= 4
    # collision


def create_game():
    # resize game window
    # boarder between game and code window
    # rect for code window
    # boilerplate code
    # rect for milestones
    # milestone text
    # milestone buttons
    # rocket movement
    pass


def main():

    # create rects to track and control game images
    white = pygame.Rect(50, 450, ROCKET_WIDTH, ROCKET_HEIGHT)
    red = pygame.Rect(50, 450, ROCKET_WIDTH, ROCKET_HEIGHT)
    # create clock to control frame rate
    clock = pygame.time.Clock()

    # game vars
    user_text = ''
    col = COLOR_INACTIVE
    active = False
    run = True
    # main game loop
    while run:
        # control the fps

        # identify events within game
        for event in pygame.event.get():
            # check if user ends the game
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INPUT_BOX.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        print(user_text)
                        user_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
        WIN.fill(GRAY)
        # draw images on window
        key_pressed = pygame.key.get_pressed()
        if active:
            col = COLOR_ACTIVE
        else:
            col = COLOR_INACTIVE
        pygame.draw.rect(WIN, col, INPUT_BOX)
        text_surface = LETTER_FONT.render(user_text, True, WHITE)

        gameplay(key_pressed, white, red)

        draw_window(text_surface, col, red, white)
        pygame.display.flip()
        clock.tick(FPS)
    # close the game window
    pygame.quit()


if __name__ == '__main__':
    main()