print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n."))


#----- String Manipulation-----

# New line
#print("Hello world! \nHello world!")

# string concatenation

#print("Hello" + " Alek!")

# Input function

#print("You are " + input("Who are you?"))

#name = input("What is your name?")
#print(len(name))


# Variables

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)



# -------- DAY 1 PROJECT --------

print("Welcome to Band Name Generator!")

person_city = input("Where did you grow up?\n")

person_pet_name = input("What is your pet's name?\n")

print("Your Band Name is: " + person_city + person_pet_name)