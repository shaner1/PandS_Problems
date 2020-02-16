#Task Week 2
# This program will calculate your BMI

#Will take inputs of height and weight from the user
height = float(input("What is your height in cm : "))
weight = float(input("What is your weight in kg: "))


#need to square the height
h2 = (height/100)**2

#bmi = weight in kg / height squared in cm
bmi = int(weight//h2)

print ("Your BMI is"), bmi