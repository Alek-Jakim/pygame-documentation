import pygame
from pygame import display

pygame.init()


WIN_WIDTH = 800
WIN_HEIGHT = 600

pygame.display.set_caption("Drawing Objects")
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Define colors as RGB tuples

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Give a background color to the display
display_surface.fill(GREEN)

# Give a background color to the display
pygame.display.flip()

# Draw various shapes on our display
# Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
pygame.draw.line(display_surface, BLUE, (100, 100), (200, 300), 1)

# Circle(surface, color, center, radius, thickness...0 for fill)
# // is floor division in Python to make sure we get integers and not floats
pygame.draw.circle(display_surface, WHITE,
                   (WIN_WIDTH // 2, WIN_HEIGHT // 2), 200, 5)
pygame.draw.circle(display_surface, BLACK,
                   (WIN_WIDTH // 2, WIN_HEIGHT // 2), 195, 0)

# Rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

pygame.quit()
