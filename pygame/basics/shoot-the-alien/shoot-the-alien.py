import pygame, os, random

pygame.init()

# Setting up the path
base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "assets/")

# Display and resolution
WIN_WIDTH = 945
WIN_HEIGHT = 600
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Shoot The Alien!")

# Define Colors
BLACK = (0, 0, 0)
GREEN = (66,103,66)
PALE_BLUE = (107,117,150)

# Mouse cursor
iron_sights_cursor = pygame.image.load(asset_path + "cursor.png")
pygame.mouse.set_visible(False)


# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
ALIEN_STARTING_VELOCITY = 3
ALIEN_ACCELERATION = .5

score = 0
player_lives = PLAYER_STARTING_LIVES

alien_velocity = ALIEN_STARTING_VELOCITY
alien_dx = random.choice([-1, 1])
alien_dy = random.choice([-1, 1])


# Set fonts
font = pygame.font.Font(asset_path + "Franxurter.ttf", 32)

# Set text
title_text = font.render("Shoot The Alien", True, PALE_BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render("Score: " + str(score), True, GREEN)
score_rect = score_text.get_rect()
score_rect.topright = (WIN_WIDTH - 50, 10)

lives_text = font.render("Lives: " + str(player_lives), True, GREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WIN_WIDTH - 50, 50)

game_over_text = font.render("Game Over!", True, PALE_BLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)

continue_text = font.render("Press any key to exit. Press Esc to quit.", True, GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 64)


# Set sound and music
click_sound = pygame.mixer.Sound(asset_path + "click_sound.wav")
miss_sound = pygame.mixer.Sound(asset_path + "miss_sound.wav")
pygame.mixer.music.load(asset_path + "background_music.wav")


# Set images
background_image = pygame.image.load(asset_path + "background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

alien_image = pygame.image.load(asset_path + "alien.png")
alien_rect = alien_image.get_rect()
alien_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)

# Game Loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # A click event is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # The alien was clicked
            if alien_rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                score += 1
                alien_velocity += ALIEN_ACCELERATION

                # Change alien direction
                prev_dx = alien_dx
                prev_dy = alien_dy
                
                while prev_dx == alien_dx and prev_dy == alien_dy:
                    alien_dx = random.choice([-1, 1])
                    alien_dy = random.choice([-1, 1])
            
            else:
                miss_sound.play()
                player_lives -= 1




    # Update HUD
    score_text = font.render("Score: " + str(score), True, GREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN)
    # Fill the surface
    display_surface.fill(BLACK)

    # Check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        
        # Pause the game until player clicks - then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            # Check if the player wants to play again
            for event in pygame.event.get():
                    # Get keys pressed
                keys = pygame.key.get_pressed()

                if event.type == pygame.MOUSEBUTTONDOWN and not keys[pygame.K_ESCAPE]:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES

                    alien_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)
                    alien_velocity = ALIEN_STARTING_VELOCITY
                    alien_dx = random.choice([-1, 1])
                    alien_dy = random.choice([-1, 1])

                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                # If player wants to quit
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    is_paused = False
                    running = False


    # Move the alien
    # It it's -1 it will move it negative * the velocity, if it's positive it will move it positive * the velocity, same for x and y coordinates
    alien_rect.x += alien_dx * alien_velocity
    alien_rect.y += alien_dy * alien_velocity


    # Bounce the alien of the edges of the display - prevent it from going outside the window
    if alien_rect.left <= 0 or alien_rect.right >= WIN_WIDTH:
        alien_dx = -1 * alien_dx
    if alien_rect.top <= 0 or alien_rect.bottom >= WIN_HEIGHT:
        alien_dy = -1 * alien_dy


    # Draw the background
    display_surface.blit(background_image, background_rect)

    # Blit the HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    # Blit assets
    display_surface.blit(alien_image, alien_rect)

    # Blit the new cursor - this must be after the alien so it goes over it
    cursor_coord = pygame.mouse.get_pos()
    display_surface.blit(iron_sights_cursor, cursor_coord)

    # Update the display
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()