# Intermediate

## 1. Class Basics

```python
# A class is like a blueprint for an object
class Dog():
    # A Python docstring is a string used to document a Python module, class, function or method
    """A class to represent a general dog
    """
    """"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts.
    """

    def __init__(self, name, gender, age):
        """Initialize attributes"""
        self.name = name
        self.gender = gender
        self.age = age

    """You always have to pass the self parameter to methods"""

    def eat(self):
        if self.gender == "male":
            print("Here " + self.name + "! Good boy!")
        else:
            print("Here " + self.name + "! Good girl!")

    def bark(self, is_loud):
        """Get the dog to speak"""
        if is_loud:
            print("WOOF WOOF WOOF")
        else:
            print("wof")

    def compute_age(self):
        """Compute the age in dog years"""
        dog_years = self.age * 7
        print(self.name + " is " + str(dog_years) + " years old!")


# Create two dog objects from the Dog class
dog_1 = Dog("Arya", "female", 3)
dog_2 = Dog("Max", "male", 12)


dog_1.eat()
dog_2.eat()

dog_1.bark(True)
dog_2.bark(False)
```

---

## 2. Inheritance Basics

```python
# A class is like a blueprint for an object
class Dog():
    # A Python docstring is a string used to document a Python module, class, function or method
    """A class to represent a general dog
    """
    """"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts.
    """

    def __init__(self, name, gender, age):
        """Initialize attributes"""
        self.name = name
        self.gender = gender
        self.age = age

    """You always have to pass the self parameter to methods"""

    def eat(self):
        if self.gender == "male":
            print("Here " + self.name + "! Good boy!")
        else:
            print("Here " + self.name + "! Good girl!")

    def bark(self, is_loud):
        """Get the dog to speak"""
        if is_loud:
            print("WOOF WOOF WOOF")
        else:
            print("wof")

    def compute_age(self):
        """Compute the age in dog years"""
        dog_years = self.age * 7
        print(self.name + " is " + str(dog_years) + " years old!")


class Beagle(Dog):
    """A class to represent a specific type of dog"""

    def __init__(self, name, gender, age, is_gun_shy):
        # Call the initialization of the super (parent) class
        super().__init__(name, gender, age)
        self.is_gun_shy = is_gun_shy

    def check_if_shy(self):
        if self.is_gun_shy:
            print("no gun pls i am good doggo")
        else:
            print("WAAAAR")

    def hunt(self):
        if not self.is_gun_shy:
            self.bark(True)
            print(self.name + " just brought back a duck.")
        else:
            print(self.name + " is a scardy cat.")

    # You can overwrite methods from the parent class, all you have to do is define the method again like below
    def bark(self, is_loud):
        if is_loud:
            print("HOOOOOWLLLL")


"""While Beagle has access to its parent class methods, the Dog class does not have access to Beagle's methods"""
beagle = Beagle("Max", "male", 13, True)

beagle.check_if_shy()
beagle.bark(False)
beagle.hunt()
```

---

## 3. Sprites and Sprite Groups

The Sprite class is intended to be used as a base class for the different types of objects in the game.

```python
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
```