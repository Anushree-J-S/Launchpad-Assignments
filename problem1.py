#Create a program that asks the user to enter their name and age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old

print("Code for problem 1")

from datetime import datetime

name=input("Enter your name:")
age=int(input("Enter your age:"))

year=int((100-age) +datetime.now().year)

print("Hey! ",name)
print("You will turn 100 in the year " ,year)