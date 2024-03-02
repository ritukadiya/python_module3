#How Do You Check The Presence Of A Key In A Dictionary?
'''
In Python, you can use the 'in' keyword
to check if a key is present in a dictionary.
'''

d = {'a': 1, 'b': 2, 'c': 3}
n=input("enter a key: ")
if n in d:
    print("Key",n,"is present.")
else:
    print("Key",n,"is not present.")