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

        class Enemy:
            def _init_(self, screen, x, y):
                self.screen = screen
                self.x = x
                self.y = y
                self.width = 40
                self.height = 40
                self.speed = random.randint(1, 3)
                self.rect = pygame.Rect(x, y, self)

                def update(self):
                    self.x -= self.speed
                    self.rect.x = self.x

                def draw(self):
                    pygame.draw.

                def is_off_screen(self):
                    return self.x < - self.width

class Platform:
    def __init__(self, x, y, width, height, color=(0,0,0)):

            def update(self):
                self.x -= self.speed
                self.rect.x = self.x

            def draw(self):
                pygame.draw.

            def is_off_screen(self):
                return self.x < - self.width

class ExpOrb:
    def _init_(self, screen, x, y):
             self.screen = screen
             self.x = x
             self.y = y
             self.radius = 8
             self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
    def draw(self):
        pygame.draw.circle(self.screen, "Yellow", (int(self.x), int(self.y)), self.radius)

def main():
    pygame.init()
    image1 = pygame.image.load("output-onlinepngtools.jpg")
    color1 = pygame.Color('black')
    pygame.mixer.music.load("https: // youtu.be / WeVLw9GJbWM")
    ground_height = 10
    ground_rect = pygame.Rect(0, 550, ground_height, ground_height)
    pygame.display.set_caption("lethally Project")
    # done: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1280, 720))
    # creates a Character from the my_character.py file
    knight = my_character.Character(screen, 100, 500)


    enemies = []
    exp_orbs =[]

    level = 1
    exp_points = 0
    exp_needed = 10
    score = 0

    try:
        font = pygame.font.Font(None, 36)
    except pygame.error:
        font = pygame.font.SysFont("Arial", 36)

    enemy_spawn_timer = 0
    enemy_spawn_delay = 120



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
            knight.x = knight.x - 5
        if pressed_keys[pygame.K_RIGHT]:
            knight.x = knight.x + 5
        if pressed_keys[pygame.K_SPACE]:
            knight.y = knight.y - 15

        knight.draw()
        pygame.draw.rect(screen, color1 , ground_rect)

        knight.update()







# don't forget the update, otherwise nothing will show up!
pygame.display.update()


main()