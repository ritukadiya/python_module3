#Write a Python program to convert a list to a tuple.
l=[1,2,3,4,5]
t=()

for i in l:
    t+=(i,)
print("list converted in to tuple: ",t)    