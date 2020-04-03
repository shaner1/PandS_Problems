#This program takes in a postive integer and applies a calculation to it. 
# It then outputs a sequence that ends in 1

#creates a list called L
mylist=[]
#take the input for the user
value = int(input("Please enter a positive integer: "))

# Adds the input to the list.
# The append wouldnt work unless I made i an int value when tring to append
mylist.append(int(value))

#starts a while loop that will stop when i reaches 1
# The next value is gotten by taking the current value and
# if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# The program ends if the current value is one., if the user enters 1 then the loop wont run
while value != 1:
    if value % 2 == 0:
        value /= 2
        mylist.append(int(value))
    else:
        value = (value*3)+1
        mylist.append(int(value))

print(mylist)

#based on andrew's feedback I tried to make my variable names more meaning full