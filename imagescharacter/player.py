import pygame
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()

#---------------------------------------
        #GENERAL SETUP
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

        #MOVEMENT ATTRIBUTES
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
#-------------------------------------------
    def import_assets(self):
        self.animations = {'back_stand': [], 'front_stand': [], 'leftside_stand': [], 'rightside_stand': [],
        'front_l': [], 'front_r': [],
        'back_l': [], 'back_r': [],
        'leftside_walk': [], 'rightside_walk': []}

        for animations in self.animations.keys():
            full_path = '../sprites_transparant2/' + animations
            self.animations[animations] = import_folder(full_path)

#---------------------------------------------
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0


        if keys[pygame.K_RIGHT]:
            self.direction.x = 1 
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

#---------------------------------------
    def move(self, dt):
        # left out how to move slower diagonally. (around 28:00)
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

#----------------------------------------
    def update(self, dt):
        self.input()
        self.move(dt)
        self.animations(dt) 
