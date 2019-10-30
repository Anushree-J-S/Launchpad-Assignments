#Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates

print("Code for problem 4")

x=[1,1,2,3,4,64,35,93,35,87,4,3]

ans=[]

for i in x:
    if i not in ans:
        ans.append(i)

print(ans)