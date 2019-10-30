#Write a program that asks the user for a sentence
#Print back to the user the same string except with the words in backward order.

print("Code for problem 5")

string="here is winter"
print(string)

x=string.split(" ")
ans=x[::-1]

for i in ans:
    print(i,end=" ")