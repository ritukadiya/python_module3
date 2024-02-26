#Write a Python program to remove duplicates from a list
l=[1,2,3,4,1,5,2,4]
l1=[]

for i in l:
    if i not in l1:
        l1.append(i)

    else:
        pass    
print(l1)