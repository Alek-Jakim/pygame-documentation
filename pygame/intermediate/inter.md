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