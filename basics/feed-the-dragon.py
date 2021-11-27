from operator import is_
import pygame
import os
import random

# Initialize pygame
pygame.init()

# Create a display surface
WIN_WIDTH = 1000
WIN_HEIGHT = 500
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Feed The Dragon!")

# Setting up the path
base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "assets/")

# Set colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 153, 34)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
game_font = pygame.font.Font(asset_path + "MangabeyRegular.otf", 52)

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5

DRAGON_BALL_VELOCITY = 10
# The balls are going to accelerate
DRAGON_BALL_ACCELERATION = .5
# When the ball goes of the screen, it's necessary to remove it and move it to the other side
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
ball_velocity = DRAGON_BALL_VELOCITY

# Set text
score_text = game_font.render("Score: " + str(score), True, GREEN, BLACK)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = game_font.render("Feed The Dragon", True, ORANGE, BLACK)
title_rect = title_text.get_rect()
title_rect.centerx = WIN_WIDTH // 2
title_rect.y = 10

lives_text = game_font.render(
    "Lives: " + str(player_lives), True, GREEN, BLACK)
lives_rect = lives_text.get_rect()
lives_rect.centerx = WIN_WIDTH - 70
lives_rect.y = 10

game_over_text = game_font.render("Game Over!", True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)

continue_text = game_font.render(
    "Press any key to play again!", True, GREEN, DARK_GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 64)


# Set sounds and music
ball_sound = pygame.mixer.Sound(asset_path + "ball_sound.wav")
miss_sound = pygame.mixer.Sound(asset_path + "miss_sound.wav")
miss_sound.set_volume(.1)

pygame.mixer.music.load(asset_path + "ftd_background_music.wav")

# Load images
dragon_image = pygame.image.load(asset_path + "dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.left = 32
dragon_rect.centery = WIN_HEIGHT // 2

dragon_ball_image = pygame.image.load(asset_path + "dragon_ball.png")
dragon_ball_rect = dragon_ball_image.get_rect()
# This is to move the ball off the screen on the right
dragon_ball_rect.x = WIN_WIDTH + BUFFER_DISTANCE
dragon_ball_rect.y = random.randint(64, WIN_HEIGHT - 32)

# Game Loop
#pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check the see if player wants to move
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_w] or keys[pygame.K_UP]) and dragon_rect.top > 60:
        dragon_rect.y -= PLAYER_VELOCITY
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and dragon_rect.bottom < WIN_HEIGHT:
        dragon_rect.y += PLAYER_VELOCITY

    # Check if dragonball is off the screen
    if dragon_ball_rect.x < 0:
        # Player missed the ball
        player_lives -= 1
        miss_sound.play()
        dragon_ball_rect.x = WIN_WIDTH + BUFFER_DISTANCE
        dragon_ball_rect.y = random.randint(64, WIN_HEIGHT - 32)
    else:
        # Move the dragonball
        dragon_ball_rect.x -= ball_velocity

    # Check for collision
    if dragon_rect.colliderect(dragon_ball_rect):
        score += 5
        ball_sound.play()
        dragon_ball_rect.x = WIN_WIDTH + BUFFER_DISTANCE
        dragon_ball_rect.y = random.randint(64, WIN_HEIGHT - 32)
        # Speed up the balls
        ball_velocity += DRAGON_BALL_ACCELERATION

    # Check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        # Here you need to pause the game loop and ask if the user wants to continue
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # The player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    dragon_rect.y = WIN_HEIGHT // 2
                    ball_velocity = DRAGON_BALL_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                # Player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    # Fill the display
    display_surface.fill(BLACK)

    # Blit the HUD (text stuff)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0, 60), (WIN_WIDTH, 60), 2)

    # Blit assets
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(dragon_ball_image, dragon_ball_rect)

    # Update text for score and lives
    score_text = game_font.render("Score: " + str(score), True, GREEN, BLACK)
    lives_text = game_font.render(
        "Lives: " + str(player_lives), True, GREEN, BLACK)

    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit
