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


    def update(self ):
        keys = pygame.key.get_pressed()
        old_x, old_y = self.x, self.y

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

class Enemy:
    def _init_(self, screen, x, y ):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = random.randint(1,3)
        self.rect = pygame.Rect(x, y, self.width, self.width, self.height)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    "Add draw for enemy here"

    def is_off_screen(self):
        return self.x < -self.width

class ExpOrb:
    def _init_(self, screen, x, y ):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = 8
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def draw (self):
        pygame.draw.circle(self.screen, YELLOW, (int (self.x), int (self.y)), self.radius)

def main():
    # turn on pygame
    pygame.init()

    image1 = pygame.image.load("output-onlinepngtools.jpg")
    color1 = pygame.Color('black')
    ground_height = 100
    ground_rect = pygame.Rect(0, HEIGHT - GROUND_HEIGHT)
    # create a screen
    pygame.display.set_caption("lethally Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1280, 720))
    # creates a character from the my_character.py file
    character = my_character.Character(screen, 100, 500)

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

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()