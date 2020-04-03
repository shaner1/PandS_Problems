#This program uses Newtons method to approximate the square root of user input value and will not run if the 
#value entered is not a positive number  

#first step is to define the square root function
def sqrt(x):
    #set the first guess the same value as the user inout value
    guess = x
    #This is to set the margin of error for the function 
    # as this is an approximation of the sqrt it will not = 0
    error = 0.001
    #need to set an initial value for i that is bigger than the margin for error to being the loop
    i = 1
    while i >= error: 
        #define the function of newton's method
     newGuess = guess - ((guess**2-(x))/ (2*guess))
     i = abs(newGuess - guess)
     #feeds the new guess of sqrt back into the function 
     # and will continue until the guess >= to the margin for error
     guess = newGuess
#when the guess is >= the margin of error the fucntion will return this value as the approx. sqrt
    return guess

#takes a value from the user to find the square root
userValue = float(input( "Please enter a postive integer: "))
#if the value is negative the function will not run
if userValue < 0:
    print("Value entered is not a positive number")
else:
    print("The approximate square of", userValue, "is", (round(sqrt(userValue),4)))