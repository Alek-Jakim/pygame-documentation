import pygame, os

# Initialize Pygame
pygame.init()


# Create a display surface
WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN_RES = (WIN_WIDTH, WIN_HEIGHT)
display_surface = pygame.display.set_mode(WIN_RES)
pygame.display.set_caption("Continuous Keyboard Movement")

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
dragon_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)




# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Move the dragon continuously
    if keys[pygame.K_LEFT]:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP]:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        dragon_rect.y += VELOCITY

    # Fill the display to avoid mirrored image effect
    display_surface.fill(BLACK)

    # Blit the assets
    display_surface.blit(dragon_image, dragon_rect)

    # Update the display surface
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# Quit Game
pygame.quit()