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
        self.velocity_y = 0

    def draw(self):
        self.screen.blit(self.image_still, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.image_still.get_width(), self.image_still.get_height())


class Platform:
    def __init__(self, x, y, width, height, color=(0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)

class Enemy:
    def _init_(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = random.randint(1, 3)
        self.rect = pygame.Rect(x, y, x, y)

    def rect(knight):
        return pygame.Rect(knight.x, knight.y,knight.image_still.get_width(),knight.image_still.get_height())

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self):
        pass
        # pygame.draw.

    def is_off_screen(self):
        return self.x < - self.width


WIDTH = 1280
HEIGHT = 720
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

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
    pygame.mixer.music.load("The Trooper (1998 Remaster).mp3")
    pygame.mixer.music.play(-1)
    ground_height = 10
    ground_rect = pygame.Rect(0, 550, ground_height, ground_height)
    pygame.display.set_caption("lethally Project")
    screen = pygame.display.set_mode((1280, 720))

    knight = Knight(screen, 100, 422)

    platform1 = Platform(0, 550, 1500, 350, )
    platform2 = Platform(0, 550, 1500, 350, )
    platforms = [platform1, platform2]


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
        if pressed_keys[pygame.K_SPACE]:
            knight.velocity_y = -15

        # TODO: use physics to move knight.y
        # TODO: apply gravity to change velocity
        # TODO: collision detection for landing on ground
        for platform in platforms:
            if knight.rect().colliderect(platform.rect) and knight.velocity_y >= 0:
                knight.y = platform.rect.top - knight.rect().height
                knight.velocity_y = 0

        knight.velocity_y +=1
        knight.velocity_y += knight.velocity_y

        knight.draw()
        pygame.draw.rect(screen, color1 , ground_rect)
            # TODO: Add you events code
        for platform in platforms:
            if knight.rect().colliderect(platform.rect) and knight.velocity_y > 0:
                knight.y = platform.rect.top - knight.rect().height
                knight.velocity_y = 0

        # TODO: Fill the screen with whatever background color you like!
 # screen.fill((255, 255, 255))

        # draws the character every frame
        #character.draw()

        # TODO: Add your project code
        for platform in platforms:
             platform.draw(screen)



        # knight.update()
        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()