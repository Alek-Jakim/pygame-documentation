#height = input("Enter your height in m: ")
#weight = input("Enter your weight in kg: ")

#bmi = int(weight) // float(height) ** 2


#print("Your BMI is ", bmi)

def bmi_calculator():
    weight = input("Enter your weight in kg: ")
    height = input("Enter your height in m: ")

    while (not height or not weight):
        weight = input("Enter your weight in kg: ")
        height = input("Enter your height in m: ")
    
    bmi = int(weight) // float(height) ** 2
    return bmi

alek_bmi = bmi_calculator()

print("Alek has a BMI of", alek_bmi)