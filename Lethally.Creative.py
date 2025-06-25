

import pygame
import sys
import my_character
import random
import time

class Knight(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, x, y):
        super(Knight, self).__init__()
        self.image = pygame.image.load("Idle.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen
        self.x = x
        self.y = y
        self.sprites = []
        self.sprites.append(pygame.image.load("Idle.png"))
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.sprites.append(pygame.image.load())
        self.velocity_y = 0
        self.health = 100

        self.max_health = 100

        self.is_attacking = False

        self.attack_cooldown = 0

        self.last_attack_time = 0

        self.attack_duration = 200


    def draw(self):
        self.screen.blit(self.image_still, (self.x, self.y))

        health_bar_width = 85

        health_bar_height = 15

        health_bar_x = self.x + 6

        health_bar_y = self.y - 15

        current_health_width = (self.health / self.max_health * health_bar_width)

        pygame.draw.rect(self.screen, (0, 0, 255),(health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        pygame.draw.rect(self.screen, (0, 255, 0),(health_bar_x,health_bar_y,current_health_width, health_bar_height))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.image_still.get_width(), self.image_still.get_height())


class Platform:
    def __init__(self, x, y, width, height, color=(0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)

class Enemy:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = random.randint(1, 3)
        self.rect = pygame.Rect(x, y, x, y)

    def update(self):
        self.rect.x -= 2

    def hit(self):
        self.alive = False
        return ExpOrb(self.screen, self.rect.centerx, self.rect.centery)

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
GRAY = (128, 128, 128)

class ExpOrb:
    def __init__(self, screen, x, y):
             self.screen = screen
             self.x = x
             self.y = y
             self.radius = 8
             self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
    def draw(self):
        pygame.draw.circle(self.screen, "Yellow", (int(self.x), int(self.y)), self.radius)

def game_over_screen(screen, score, level, song_length):
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(BLACK)
        msg = font.render("GAME OVER", True, RED)
        score_msg = small_font.render(f"Score: {score}", True, WHITE)
        level_msg = small_font.render(f'Level Reached: {level}', True, WHITE)
        rentry_msg = small_font.render('Press R to Retry or Q to Quit', True, GRAY)

        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 200))
        screen.blit(score_msg, (WIDTH // 2 - score_msg.get_width() // 2, 280))
        screen.blit(level_msg, (WIDTH // 2 - level_msg.get_width() // 2, 320))
        screen.blit(rentry_msg, (WIDTH // 2 - rentry_msg.get_width() // 2, 380))
        pygame.display.flip()



def main():
    pygame.init()
    image1 = pygame.image.load("output-onlinepngtools.jpg")
    color1 = pygame.Color('black')
    pygame.mixer.music.load("The Trooper (1998 Remaster).mp3")
    pygame.mixer.music.play()
    song_length = pygame.mixer.Sound("The Trooper (1998 Remaster).mp3").get_length()
    #This file came from a YouTube video: https://youtu.be/4VZbjrDwQ28
    start_time = time.time()
    sprite = Knight(screen, 100, 100)


    ground_height = 10
    ground_rect = pygame.Rect(0, 550, ground_height, ground_height)
    pygame.display.set_caption("Skeleton Slayer")
    screen = pygame.display.set_mode((1280, 720))

    knight = Knight(screen, 100, 400)

    platform1 = Platform(0, 550, 1500, 350, )
    platform2 = Platform(0, 550, 1500, 350, )
    platforms = [platform1, platform2]


    enemies = []


    enemies = [Enemy(screen, random.randint(600, 1200), 510) for _ in range(3)]


    exp_orbs =[]

    level = 1
    exp_points = 0
    exp_needed = 10
    score = 0
    exp = 0

    try:
        font = pygame.font.Font(None, 36)
    except pygame.error:
        font = pygame.font.SysFont("Arial", 36)

    enemy_spawn_timer = 0
    enemy_spawn_delay = 120

    gravity = 1

    ground_y = 400



    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        elapsed_time = time.time() - start_time
        if elapsed_time >= song_length:
            return game_over_screen(screen, score, level, song_length)


        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit()
                #sys.exit()
            #if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    #elapsed_time = song_length + 1
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_q:
                    #pygame.quit()
                #sys.exit()
            #elif event.key == pygame.K_r:
                #return True




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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and knight == ground_y:
                knight.velocity_y = -15

        # TODO: use physics to move knight
        knight.y += knight.velocity_y


        if knight.y > ground_y:
            knight.y = ground_y

            knight.velocity_y = 0



        if pressed_keys[pygame.K_SPACE] and knight.velocity_y == 0:
            knight.velocity_y = -10

        knight.velocity_y += 1
        knight.y += knight.velocity_y
        # TODO: use physics to move knight.y

        # TODO: apply gravity to change velocity
        # TODO: collision detection for landing on ground
        for platform in platforms:
            if knight.rect().colliderect(platform.rect) and knight.velocity_y >= 0:
                knight.y = platform.rect.top - knight.rect().height
                knight.velocity_y = 0

        knight.draw()
        for platform in platforms:
            platform.draw(screen)



            # TODO: Add you events code





        # TODO: Add your project code
        for platform in platforms:
             platform.draw(screen)


        for enemy in enemies[:]:
            enemy.update()
        #if knight.rect().colliderect(enemy.rect) and enemy.alive:
            exp_orbs.append(enemy.hit())
            score += 20
            if not enemy.alive:
                enemies.remove(enemy)
            #else:
               # enemy.draw()

       # for enemy in enemies[:]:
            #enemy.update()
        #if knight.rect().colliderect(enemy.rect) and enemy.alive:
            #exp_orbs.append(enemy.hit())
            #score += 20
            #if not enemy.alive:
                #enemies.remove(enemy)
            #else:
                #enemy.draw()

        #if knight.rect().colliderect(enemy.rect) and enemy.alive:
            #if not enemy.alive:
            #enemies.remove(enemy)
            #else:
                #enemy.draw()

        for orb in exp_orbs:
            if knight.rect().colliderect(orb.rect):
                exp_orbs.remove(orb)
                exp += 1
                score += 10
                if exp >= exp_needed:
                    exp = 0
                    level += 1
                    exp_needed += 5
        for orb in exp_orbs:
            orb.draw()

        remaining_time = max(0, int(song_length - elapsed_time))
        #timer_display = font.render(f"Time: {remaining_time}", True, BLACK)
        level_display = font.render(f"Level: {level}", True, BLACK)
        score_display = font.render(f"Score: {score}", True, BLACK)
        #exp_display = font.render(f"Exp: {exp}/{exp_needed}", True, BLACK)

        #screen.blit(timer_display, (10, 10))
        screen.blit(level_display, (10,40))
        screen.blit(score_display, (10, 70))
        #screen.blit(exp_display, (10, 100))
        # knight.update()
        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()