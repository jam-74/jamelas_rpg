import pygame, sys
from level import Level


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TITLE_SIZE = 64


#----------------------

#DISPLAYS THE GAME
class Game: 
    def __init__(self):
        pygame.init() #INIT METHOD
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('CODEMON ≧◔◡◔≦')
        self.clock = pygame.time.Clock()
        self.level = Level()

  
    def run(self):
        while True: #GAME LOOP
            for event in pygame.event.get(): #CLOSES THE GAME
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000 #DELTA TIME
            self.level.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()                        