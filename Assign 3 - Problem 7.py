#Commented by Nousheen Siddiqui
#Edited on 1/29/2021
#The program calculates the lenght of the stay and the return day of the week
#if the start day is provided

startday = int(input("Enter the start day"))
lengthday = int(input("Enter the lenght of your stay"))
returnday = (startday+lengthday)% 7 # % is 13%7 which is the 6th day.
print ("returnday",returnday)
