from pickle import REDUCE

import pygame
import sys
import my_character
import random
import time

class Character:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_still = pygame.image.load("Idle.png")

    def draw(self):
        self.screen.blit(self.image_still, (self.x, self.y))

WIDTH = 1280
HEIGHT = 720
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GROUND_HEIGHT= 100

class Character:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update(self ):
        keys = pygame.key.get_pressed()
        old_x, old_y = self.x, self.y

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed

        


class Platform:
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

def main():
    # turn on pygame
    pygame.init()

    image1 = pygame.image.load("output-onlinepngtools.jpg")
    color1 = pygame.Color('black')
    ground_height = 100
    ground_rect = pygame.Rect(0, HEIGHT - ground_height)
    # create a screen
    pygame.display.set_caption("lethally Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1280, 720))
    # creates a Character from the my_character.py file
    character = my_character.Character(screen, 100, 500)

    platform1 = Platform(0, 550, 1500, 350, )
    platform2 = Platform(0, 550, 1500, 350, )
    platforms = [platform1, platform2]

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(image1, (0, 0))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            character.x = character.x - 5
        if pressed_keys[pygame.K_RIGHT]:
            character.x = character.x + 5
        if pressed_keys[pygame.K_SPACE]:
            character.y = character.y - 15

        character.draw()



    pygame.draw.rect( screen, color1 , gorund_rect )
            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        # screen.fill((255, 255, 255))

        # draws the character every frame
        #character.draw()

        # TODO: Add your project code
        for platform in platforms:
            platform.draw(screen)

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()







main()