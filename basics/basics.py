import pygame, os

# Initiallize Pygame
pygame.init()

# Create a display surface

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN_RES = (WIN_WIDTH, WIN_HEIGHT)
display_surface = pygame.display.set_mode(WIN_RES)
pygame.display.set_caption("Mouse Events")

# Setting up the path
base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "assets/")

# Load Images
dragon_image = pygame.image.load(asset_path + "dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move based on mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.center = (mouse_x, mouse_y)

        # Move the object to follow the mouse
        # This and statement makes you drag the object by holding down the mouse click (in this case it's the left click --- see print(event.buttons))
        # <Event(1024-MouseMotion {'pos': (x, y), 'rel': (1, 0), 'buttons': (1, 0, 0), 'touch': False, 'window': None})>
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                print(event)
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                dragon_rect.center = (mouse_x, mouse_y)


    # Fill the display
    display_surface.fill((0, 0, 0))

    # Blit the image on the screen surface
    display_surface.blit(dragon_image, dragon_rect)

    # Update the display surface
    pygame.display.update()
# End Game
pygame.quit()