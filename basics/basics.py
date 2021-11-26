import pygame, os

# Initialize pygame
pygame.init()


# Create display surface
WIN_WIDTH = 600
WIN_HEIGHT = 300
WIN_RES = (WIN_WIDTH, WIN_HEIGHT)

pygame.display.set_caption("Keyboard Movement")
display_surface = pygame.display.set_mode(WIN_RES)

# Define Colors

BLACK = (0, 0, 0)

# Setting up the path
base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "assets/")

# Set game values
VELOCITY = 20

# Load in images
dragon_image = pygame.image.load(asset_path + "dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WIN_WIDTH // 2
dragon_rect.bottom = WIN_HEIGHT

# Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY

    # Fill the display surface to cover old images
    # If you don't do this it will leave the old images and it will look like Killua
    display_surface.fill(BLACK)

    # Blit assets to the screen
    display_surface.blit(dragon_image, dragon_rect)

    # Update display
    pygame.display.update()


# End Game
pygame.quit()