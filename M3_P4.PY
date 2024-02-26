#Write a Python function to get the largest number, smallest num and sum of all from a list.
list=[]
n=int(input("enter a total number of list element: "))

for i in range(1,n+1):
    value=int(input("please enter a value of elment: "))
    list.append(value)

print("list: ",list)
print("the smallest element in this list is: ",min(list))
print("the largest element in this list: ",max(list))
print("total sum of all element: ",sum(list))    
 