import pygame
import random
from settings import *
from classes import *

# Initialize pygame
pygame.init()

# Set display


display_surface = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Monster Wrangler")


# Set FPS and Clock
clock = pygame.time.Clock()

# Create a player group and object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

# Create a monster group
my_monster_group = pygame.sprite.Group()

# TEST MONSTER
monster = Monster(500, 500, pygame.image.load(
    asset_path + "green_monster.png"), 1)
my_monster_group.add(monster)
monster = Monster(500, 500, pygame.image.load(
    asset_path + "blue_monster.png"), 1)
my_monster_group.add(monster)


# Create a game object
my_game = Game(my_player, my_monster_group)


# Main game loop
running = True

while running:
    # Check if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill display
    display_surface.fill((0, 0, 0))

    # Update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    # Update and draw game
    my_game.update()
    my_game.draw()

    # Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End game
pygame.quit()
