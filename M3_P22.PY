#Write a Python program to check whether an element exists within a tuple.
t=(1,2,3,4,5,6,7)

n=int(input("enter a number to check: "))
if n in t:
    print(n,"exist in tuple")
else:
    print(n,"not exist in tuple")    