import pygame
import os
import random

# Initialze pygame
pygame.init()

# Set path

base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "game_assets/")

# Set display surface
WIN_WIDTH = 800
WIN_HEIGHT = 600
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sprite Groups!")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Define Classes


class Monster(pygame.sprite.Sprite):
    """A simple class that represents a monster"""

    def __init__(self, x, y):
        # Since this is a subclass of the Sprite class, you have to use super
        super().__init__()
        self.image = pygame.image.load(asset_path + "blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        """Update and move the monster"""
        self.rect.y += self.velocity


# Create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
for i in range(10):
    # Don't forget to pass x and y inside Monster(x, y)
    monster = Monster(i * 64, 10)
    monster_group.add(monster)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    # Fill the display
    display_surface.fill((0, 0, 0))

    # Update and Draw assets
    monster_group.update()
    monster_group.draw(display_surface)

    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

# End the game - this is optional if you have exit() after clicking quit
pygame.quit()
