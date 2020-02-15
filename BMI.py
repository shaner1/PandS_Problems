#This program will calculate your BMI

height = float(input("What is your height in cm : "))
weight = float(input("What is your weight in kg: "))

h2 = (height/100)**2
bmi = int(weight//h2)

print ("Your BMI is"), bmi