#This program will take a user input of a file name and output the amount of "e" it contains

textfile = input("Filename: ")

with open(textfile, 'r') as reader:
    text = reader.read()
    count = 0
    for i in text: 
        if i == "e": 
            count = count + 1
    print("This file contains",count ,"of the letter e")
  
