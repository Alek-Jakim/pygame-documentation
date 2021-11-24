import pygame, os

# Init pygame
pygame.init()

# Setting up the path
base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "assets/")

# Create a display surface
WIN_WIDTH = 600
WIN_HEIGHT = 300
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Adding Sounds and Music")


# Load sound effects
sound_1 = pygame.mixer.Sound(asset_path + "sound_1.wav")
sound_2 = pygame.mixer.Sound(asset_path + "sound_2.wav")

# Play sound effects 
sound_1.play()
# If you don't delay the time (here 2 seconds) it will only play the last sound that is called
pygame.time.delay(2000)

# Change the volume of a sound effect
sound_2.set_volume(.1)
sound_2.play()

# Load background music
pygame.mixer.music.load(asset_path + "music.wav")

# Play and stop the music
# pygame.mixer.music.play() takes two arguments, first is how many tims you wanna loop, for example 1, 2, 3 etc (-1 for infinite loop), second argument is when do you want it to start
pygame.mixer.music.play(-1) 
pygame.time.delay(5000)
pygame.mixer.music.stop()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# End the game
pygame.quit()
