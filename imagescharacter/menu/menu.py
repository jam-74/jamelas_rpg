import pygame
import button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TITLE_SIZE = 64

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CODEMON ≧◔◡◔≦')

#game variables
game_paused = False

#font
font = pygame.font.SysFont('arialblack', 40) 

#colours
TEXT_COLOUR = (255, 255, 255)

#load image
resume_img = pygame.image.load('besume.png').convert_alpha()
quit_img = pygame.image.load('quit.png').convert_alpha() 
#create button instances
resume = button.Button(304, 125, resume_img, 1)
quit = button.Button(104, 505, quit_img, 1)

def draw_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    screen.blit(img, (x, y))

run = True   
while run:

    screen.fill((52, 78, 91))

    #check if game is paused
    if game_paused == True:
        resume.draw(screen)
        quit.draw(screen)
        #display menu
    else:
        draw_text('Press SPACE to pause', font, TEXT_COLOUR, 400, 300)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
