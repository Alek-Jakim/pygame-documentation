# Basics

## 1. Creating a Display Surface

```python
import pygame

# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
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
```
---
## 2. Drawing on a Display Surface

**Important Note:**

* `display.flip()` will update the contents of the entire display

* `display.update()` allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display

```python
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
```

---

## 3. Blitting (copying) Images

```python
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
```
---

## 4. Blitting (copying) Text

```python
import pygame, os

# Initiate Game
pygame.init()

# Display Surface
WIN_WIDTH = 800
WIN_HEIGHT = 600
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Blitting Images!")

# Define colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setting up the path
base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "assets/")

# See all available system fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

# Define Fonts
system_font = pygame.font.SysFont("calibri", 64)
custom_font = pygame.font.Font(asset_path + "AttackGraffiti.ttf", 32)

# Define Text (text content, boolean True for antialiasing, color, background(not mandatory))
# NOTE: When I don't provide a background color, it becomes the same color as the text so it can't be seen.
system_text = system_font.render("To be or not to be", True, GREEN, DARK_GREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT //2)

custom_text = custom_font.render("Move the dragon soon!", True, WHITE, BLACK)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100)


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the text onto the screen
    display_surface.blit(system_text, system_text_rect)

    display_surface.blit(custom_text, custom_text_rect)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
```

---

## 5. Adding Sound Effects and Music

```python
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
```
---

## 6. Discrete Keyboard Movement

```python
import pygame, os

# Initialize pygame
pygame.init()


# Create display surface
WIN_WIDTH = 600
WIN_HEIGHT = 300
WIN_RES = (WIN_WIDTH, WIN_HEIGHT)

pygame.display.set_caption("Keyboard Movement")
display_surface = pygame.display.set_mode(WIN_RES)

# Define Colors

BLACK = (0, 0, 0)

# Setting up the path
base_path = os.path.dirname(__file__)
asset_path = os.path.join(base_path, "assets/")

# Set game values
VELOCITY = 20

# Load in images
dragon_image = pygame.image.load(asset_path + "dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WIN_WIDTH // 2
dragon_rect.bottom = WIN_HEIGHT

# Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY

    # Fill the display surface to cover old images
    # If you don't do this it will leave the old images and it will look like Killua
    display_surface.fill(BLACK)

    # Blit assets to the screen
    display_surface.blit(dragon_image, dragon_rect)

    # Update display
    pygame.display.update()


# End Game
pygame.quit()
```

--- 

## 7. Mouse Movement

```python
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
```

---

## 8. Continuous Keyboard Movement (FPS)

```python
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
```

---

## 9. Movement Restriction and Alternative Keymapping

```python
# Same code as the code block above (8. Continuous Keyboard Movement (FPS)) except:

# Getting the rect coordinates to make sure the object doesn't move off screen
if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WIN_WIDTH:
        dragon_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WIN_HEIGHT:
        dragon_rect.y += VELOCITY
```


---

## 10. Collision Detection

```python
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
        # This will make the coin dissappear and reappear at a random position once the dragon touches it
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
```