import pygame
import os

# Initialize pygame
pygame.init()

# Create a display surface
WIN_WIDTH = 800
WIN_HEIGHT = 600
WIN_RESOLUTION = (WIN_WIDTH, WIN_HEIGHT)
pygame.display.set_caption("Blitting!")
display_surface = pygame.display.set_mode(WIN_RESOLUTION)

#This is to get the correct path to the assets
base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "assets/")

# Create images - returns a surface object with the image drawn on it
# We can then get the rect of the surface and use the rect to position the image
dragon_left_image = pygame.image.load(image_path + "dragon_left.png") 
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load(image_path + "dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WIN_WIDTH, 0)

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) a surface object at the given coordinates to my display
    # Blit takes two args, the image and the coordinates of the image
    # NOTE: You have to do this in order for the images to show!
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    # Update the display
    pygame.display.update()

# End the game
pygame.quit()