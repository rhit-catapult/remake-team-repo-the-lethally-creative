from pickle import REDUCE

import pygame
import sys
import my_character
import random
import time

class Knight:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_still = pygame.image.load("Idle.png")

    def draw(self):
        self.screen.blit(self.image_still, (self.x, self.y))

def main():
    pygame.init()
    image1 = pygame.image.load("output-onlinepngtools.jpg")
    color1 = pygame.Color('black')
    ground_height = 10
    ground_rect = pygame.Rect(0, 550, ground_height, ground_height)
    pygame.display.set_caption("lethally Project")
    screen = pygame.display.set_mode((1280, 720))
    knight = my_character.Character(screen, 100, 550)


    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(image1, (0, 0))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            knight.x = knight.x - 5
        if pressed_keys[pygame.K_RIGHT]:
            knight.x = knight.x + 5
        
        knight.draw()
        pygame.draw.rect(screen, color1 , ground_rect)
            # TODO: Add you events code

        # TODO: Add your project code

        pygame.display.update()


main()