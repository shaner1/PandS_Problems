#This program will take a user input of a file name and output the amount of "e" it contains

textfile = input("Please enter myfile.txt: ") #this will take the users input and use it as the file name to be read 

with open(textfile, 'r') as reader: # opens the text file provided by user
    text = reader.read() # read the text file 
    count = 0 # sets the counter to 0
    for letters in text: 
        if letters == "e":  
            count = count + 1 
    # sets a for loop that reads through the text file 
    # and increments the counter everytime it finds the letter e
    print("This file contains",count ,"of the letter e.") 
    # print out the amount of the letter e in the file 
  
#I tried to print a list of all readable files for the user to pick but it didnt work