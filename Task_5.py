#This program will let you know whether it is a week day or not 

#Import the library Datetime
import datetime

message1= ("Today is a Weekday")
message2= ("Today is the Weekend :)")

now = datetime.datetime.now()

#Define the variable day
day = now.weekday()

#If day is less than 4, than it will be a weekday.  
if day < 4:
    print(message1)
else:
    print(message2)

