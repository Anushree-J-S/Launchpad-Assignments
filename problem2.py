#write a program that prints out all the elements of the list that are less than 5

print("Code for problem 2")

x=[1,1,2,3,5,8,13,21,34,55,89]

new_list=[]

for i in x:
    if i<5:
        new_list.append(i)

print(new_list)