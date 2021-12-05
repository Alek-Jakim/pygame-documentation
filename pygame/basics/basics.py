import pygame, os, random

# Initialize Pygame
pygame.init()


# Create a display surface
WIN_WIDTH, WIN_HEIGHT = 600, 300
WIN_RES = (WIN_WIDTH, WIN_HEIGHT)
display_surface = pygame.display.set_mode(WIN_RES)
pygame.display.set_caption("Collision Detection")

# Setting up the path
base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "assets/")


# Set FPS and clock
# This it to make sure the game runs the same on any machine
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

# Define Colors
BLACK = (0, 0, 0)

# Load images
dragon_image = pygame.image.load(asset_path + "dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

coin_image = pygame.image.load(asset_path + "coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_d] and dragon_rect.right < WIN_WIDTH:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_w] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_s] and dragon_rect.bottom < WIN_HEIGHT:
        dragon_rect.y += VELOCITY

    # Fill display surface
    display_surface.fill(BLACK)


    # Check for collision between two rects
    if dragon_rect.colliderect(coin_rect):
        # You subtract the image pixels from the window width because it will be off screen if it's just WIN_WIDTH
        coin_rect.x = random.randint(0, WIN_WIDTH - 32)
        coin_rect.y = random.randint(0, WIN_HEIGHT - 32)

    # Draw rectangle to represent the rect's of each object - this is just for visual representation to see where the rect's are exactly
    pygame.draw.rect(display_surface, (0, 255, 0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255, 0, 0), coin_rect, 1)
    # Blit assets
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)


# Quit Game
pygame.quit()


# NOTE: Check how to flip the image (pygame.transform.flip())