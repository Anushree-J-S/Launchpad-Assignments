#Given a element, search the entire list for the element and return the indices that match the list

print("Code for problem 3")

x=[1,2,3,2,0,65,21,4,2,10]

indices_list=[]

for i in range(0,len(x)):
    if x[i]==2:
        indices_list.append(i)

print(indices_list)