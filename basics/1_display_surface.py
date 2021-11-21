import pygame

# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.display.set_caption("Game Title!")

display_surface = pygame.display.set_mode(WINDOW_SIZE)

# The main game loop
running = True

while running:
    # Loop through a list of event objects that have occured (check your console when running the program)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# End the game
pygame.quit()
