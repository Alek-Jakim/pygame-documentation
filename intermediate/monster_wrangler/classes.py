import pygame
from settings import *
import random


class Game():
    """A class to control gameplay"""

    def __init__(self, player, monster_group):
        """Initialize game object"""
        # Set game values
        self.score = 0
        self.round_number = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.monster_group = monster_group

        # Set sounds and music
        self.next_level_sound = pygame.mixer.Sound("next_level.wav")
        self.font = pygame.font.Font("Abrushow.ttf", 24)

        # Set images
        blue_image = pygame.image.load("blue_monster.png")
        green_image = pygame.image.load("green_monster.png")
        purple_image = pygame.image.load("purple_monster.png")
        yellow_image = pygame.image.load("yellow_monster.png")
        # This list corresponds to the monster type attribute (the reason why we assign integers)
        self.target_monster_images = [blue_image,
                                      green_image, purple_image, yellow_image]

        self.target_monster_type = random.randint(0, 3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = WIN_WIDTH // 2
        self.target_monster_rect.top = 30

    def update(self):
        """Update game object"""
        self.round_time += 1

        # Check for collisions
        self.check_collisions()

    def draw(self):
        """Draw the HUD and other to display"""
        # Set colors
        WHITE = (255, 255, 255)
        BLUE = (20, 176, 235)
        GREEN = (87, 201, 47)
        PURPLE = (226, 73, 243)
        YELLOW = (243, 157, 20)

        # Add monster colors to a list where the index of the color matches target_monster_images
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        # Set text
        catch_text = self.font.render()
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = WIN_WIDTH // 2
        catch_rect.top = 5

        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        lives_text = self.font.render(
            "Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)

        round_text = self.font.render(
            "Current Round: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft(5, 65)

    def check_collisions(self):
        """Check for collisions between player and monsters"""
        pass

    def start_new_round(self):
        """Populate board with new monsters"""
        pass

    def choose_new_target(self):
        """Choose a new target monster for player"""
        pass

    def pause_game(self):
        """Pause game duuh"""
        pass

    def reset_game(self):
        """Reset game duuh"""
        pass


class Player(pygame.sprite.Sprite):
    """Player class controlled by user"""

    def __init__(self):
        """Initialize player"""
        super().__init__()
        self.image = pygame.image.load(asset_path + "knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIN_WIDTH // 2
        self.rect.bottom = WIN_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound(
            asset_path + "catch.wav")
        self.die_sound = pygame.mixer.Sound(asset_path + "die.wav")
        self.warp_sound = pygame.mixer.Sound(asset_path + "warp.wav")

    def update(self):
        """Update Player"""
        keys = pygame.key.get_pressed()

        # Move player withing bounds of screen
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.velocity
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self. rect.right < WIN_WIDTH:
            self.rect.x += self.velocity
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.top > 0:
            self.rect.y -= self.velocity
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self. rect.bottom < WIN_HEIGHT:
            self.rect.y += self.velocity

    def warp(self):
        """Warp the player to the safe zone"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WIN_HEIGHT

    def reset(self):
        """Resets player position"""
        self.rect.centerx = WIN_WIDTH // 2
        self.rect.bottom = WIN_HEIGHT


class Monster(pygame.sprite.Sprite):
    """A class to create enemy monster objects"""

    def __init__(self, x, y, image, monster_type):
        """Initialize the monster"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Monster type ints 0 = blue, 1 = green, 2 = purple, 3 = yellow (See under Game class -> self.target_monster_images)
        self.type = monster_type

        # Set random motion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)

    def update(self):
        """Update the monster"""
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity

        # Bounce the monster off the edges of display
        if self.rect.left <= 0 or self.rect.right >= WIN_WIDTH:
            self.dx = -1 * self.dx
        if self.rect.top <= 0 or self.rect.bottom >= WIN_HEIGHT:
            self.dy = -1 * self.dy
