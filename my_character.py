import pygame
import sys


class Character:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_still = pygame.image.load("Idle.png")

    def draw(self):
        self.screen.blit(self.image_still, (self.x, self.y))

# This function is called when you run this file, and is used to test the character class individually.
# When you create more files with different classes, copy the code below, then
# change it to properly test that class
def test_character():
    # TODO: change this function to test your class
    screen = pygame.display.set_mode((640, 480))
    character = Character(screen, 400, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        for event in pygame.event.get():
            # TODO 4:   Make the pygame.QUIT event stop the game.
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            character.x = character.x - 2
        if pressed_keys[pygame.K_RIGHT]:
            character.x = character.x + 2
        if pressed_keys[pygame.K_UP]:
            character.y = character.y - 2
        if pressed_keys[pygame.K_DOWN]:
            character.y = character.y + 2

        screen.fill("white")
        character.draw()
        pygame.display.update()


# Testing the classes
# click the green arrow to the left or run "Current File" in PyCharm to test this class
if __name__ == "__main__":
    test_character()
