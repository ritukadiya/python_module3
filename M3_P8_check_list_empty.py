#Write a Python program to check a list is empty or not.
def Info(l1):
    if len(l1)==0:
        return 0
    else:
        return 1
 

l1=input("enter a value:")
if Info(l1):
    print("The List is Not Empty")
else:
    print("Empty List")