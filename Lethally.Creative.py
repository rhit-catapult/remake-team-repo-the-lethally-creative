

import pygame
import sys
import my_character
import random
import time

class Knight:
    def __init__(self, screen: pygame.Surface, x, y, idle_filename, attack_filename):
        self.image = pygame.image.load(idle_filename)
        #This Knight sprite was acquired by Owyn Steele at the Website https://craftpix.net
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen
        self.x = x
        self.y = y
        self.image_attack = pygame.image.load(attack_filename)
        # This Knight sprite was acquired by Owyn Steele at the Website https://craftpix.net
        self.velocity_y = 0
        self.health = 100
        self.max_health = 100
        self.is_attacking = False
        self.is_not_attacking = True
        self.attack_cooldown = 0
        self.last_attack_time = 0
        self.attack_duration = 200
        #This sprite came from craftpix-net-803217-free-knight-character-sprites-pixel-art.zip
        self.attack_frame_index = 0
        self.last_frame_update = pygame.time.get_ticks()
        self.animation_speed = 100
        self.facing_right = True

        self.hit_points = 3
        self.last_hit_time = 0




    def get_attack_hitbox(self):
            if self.is_attacking:


                attack_width = 70

                attack_height = 50

                return pygame.Rect(self.x + self.image.get_width() / 2,
                                   self.y + self.image.get_height() / 4, attack_width, attack_height)

            return None


    def draw(self):
        health_bar_width = 50

        health_bar_height = 15

        health_bar_x = self.x + 15

        health_bar_y = self.y - 10

        current_health_width = (self.hit_points // 3) * health_bar_width

        health_bar_width = 50
        health_bar_height = 15
        health_bar_x = self.x
        health_bar_y = self.y -15

        current_health_width = self.hit_points * health_bar_width//3

        pygame.draw.rect(self.screen, (50, 50, 50),(health_bar_x, health_bar_y, health_bar_width, health_bar_height))

        if self.hit_points == 3:
            bar_color = (0, 255, 0)  # Green
        elif self.hit_points == 2:
            bar_color = (255, 255, 0)  # Yellow
        elif self.hit_points == 1:
            bar_color = (255, 0, 0)#red
        else:
            bar_color = (0, 0, 0)  # invisible

        if not self.is_attacking:
            current_image = self.image
        if self.is_attacking:
            current_image = self.image_attack
        if not self.facing_right:
            current_image = pygame.transform.flip(current_image, True, False)

        self.screen.blit(current_image, (self.x, self.y))

        if self.hit_points > 0:
            pygame.draw.rect(self.screen, bar_color, (health_bar_x, health_bar_y, current_health_width, health_bar_height))

        # Draw health bar background (gray for neutral)
        pygame.draw.rect(self.screen, (50, 50, 50),
                         (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        # Draw actual health
        pygame.draw.rect(self.screen, bar_color,
                         (health_bar_x, health_bar_y, current_health_width, health_bar_height))

        if self.hit_points == 3:
                bar_color = (0,255, 0)
        elif self.hit_points == 2:
                bar_color = (255, 255, 0)
        else:
                bar_color = (255, 0, 0)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def attack(self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_attack_time >= self.attack_cooldown:
            self.is_attacking = True

            self.attack_frame_index = 0

            self.last_frame_update = current_time

            self.last_attack_time = current_time

            return True

        return False

    def set_direction(self, facing_right):
        self.facing_right = facing_right



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
        self.size = 40
        self.speed = random.randint(2, 5) * random.choice([-1, 1])
        self.alive = True
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed *= -1

    def draw(self):
        if self.alive:
            pygame.draw.rect(self.screen, RED, (self.x, self.y, self.size, self.size ))

    def hit(self):
        self.alive = False
        return ExpOrb(self.screen, self.x + self.size // 2, self.y + self.size //2)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    main()
                    return






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
    #This image from YouTube video: https://www.youtube.com/watch?v=wZo45IPcBug
    #This Background is an image Owyn found online and pixelated with onlinetools.com.
    color1 = pygame.Color('black')
    pygame.mixer.music.load("The Trooper (1998 Remaster).mp3")
    pygame.mixer.music.play()
    song_length = pygame.mixer.Sound("The Trooper (1998 Remaster).mp3").get_length()
    #This file came from a YouTube video: https://youtu.be/4VZbjrDwQ28
    start_time = time.time()


    ground_height = 10
    ground_rect = pygame.Rect(0, 550, ground_height, ground_height)
    pygame.display.set_caption("Slime Slayer")
    screen = pygame.display.set_mode((1280, 720))

    knight = Knight(screen, 100, 400, "Idle.png", "Attack 3.png")

    platform1 = Platform(0, 550, 1500, 350, )
    platforms = [platform1]

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


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    game_over_screen(screen, score, level, song_length)
                    return
                if event.key == pygame.K_a:
                        knight.is_attacking = True
                        Knight.is_not_attacking = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                        knight.is_attacking = False
                        knight.is_not_attacking = True



        enemy_spawn_timer += 1

        if enemy_spawn_timer >= enemy_spawn_delay:
            new_enemy = Enemy(screen, random.randint(0, WIDTH - 40), 510)

            enemies.append(new_enemy)

            enemy_spawn_timer = 0

            enemy_spawn_delay = random.randint(60, 180)

        screen.blit(image1, (0, 0))



        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            knight.x = knight.x - 5
            knight.facing_right = False
        if pressed_keys[pygame.K_RIGHT]:
            knight.x = knight.x + 5
            knight.facing_right = True

        clamp_margin = 20
        knight.x = max(0,min (knight.x, WIDTH - clamp_margin))

        knight.rect.topleft =(knight.x, knight.y)


        knight_width = knight.image.get_width()
        knight_height = knight.image.get_height()


        knight_width = knight.image.get_width()
        knight_height = knight.image.get_height()
        knight.x = max(0, min(knight.x, WIDTH - knight_width))




        # TODO: use physics to move knight
        knight.velocity_y += 1
        knight.y += knight.velocity_y

        knight.rect.topleft = (knight.x, knight.y)

        grounded = False
        for platform in platforms:


            if knight.rect.colliderect(platform.rect):

                knight.y = platform.rect.top - knight.rect.height

                knight.velocity_y = 0
                grounded = True
                break

        if pressed_keys[pygame.K_SPACE] and grounded:
            knight.velocity_y = -15
# TODO: use physics to move knight.y

        # TODO: apply gravity to change velocity
        # TODO: collision detection for landing on ground
        for platform in platforms:
            if knight.rect.colliderect(platform.rect) and knight.velocity_y >= 0:
                knight.y = platform.rect.top - knight.rect.height
                knight.velocity_y = 0

        knight.draw()
        for platform in platforms:
            platform.draw(screen)

            if knight.is_attacking:

                attack_hitbox = knight.get_attack_hitbox()

                if attack_hitbox:

                    for enemy in enemies[:]:

                        if attack_hitbox.colliderect(enemy.rect):



                            if hasattr(enemy, 'alive') and enemy.alive:

                                exp_orbs.append(enemy.hit())

                                score += 20



                                if not enemy.alive:
                                    enemies.remove(enemy)



            # TODO: Add you events code







        # TODO: Add your project code
        for platform in platforms:
             platform.draw(screen)

        for enemy in enemies[:]:
            enemy.update()
            enemy.draw()
            if knight.rect.colliderect(enemy.rect) and enemy.alive:
                current_time = pygame.time.get_ticks()
                if current_time - knight.last_hit_time > 1000:
                    knight.hit_points -= 1
                    knight.health = knight.hit_points / 3 * knight.max_health
                    knight.last_hit_time = current_time
                    if knight.hit_points <= 0:
                        return game_over_screen(screen, score, level, song_length)

        if knight.rect.colliderect(enemy.rect) and enemy.alive:
            if not enemy.alive:
                enemies.remove(enemy)
            else:
                enemy.draw()

        for orb in exp_orbs:
            if knight.rect.colliderect(orb.rect):
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
        timer_display = font.render(f"Time: {remaining_time}", True, BLACK)
        level_display = font.render(f"Level: {level}", True, BLACK)
        score_display = font.render(f"Score: {score}", True, BLACK)
        exp_display = font.render(f"Exp: {exp}/{exp_needed}", True, BLACK)

        screen.blit(timer_display, (10, 10))
        screen.blit(level_display, (10,40))
        screen.blit(score_display, (10, 70))
        screen.blit(exp_display, (10, 100))
        # knight.update()
        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()