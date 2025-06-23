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

def main():
    # turn on pygame
    pygame.init()

    image1 = pygame.image.load("output-onlinepngtools.jpg")

    # create a screen
    pygame.display.set_caption("lethally Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1280, 720))
    # creates a Character from the my_character.py file
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



            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
 # screen.fill((255, 255, 255))

        # draws the character every frame
        #character.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()