# Write a Python program to remove an empty tuple(s) from a list of tuples.
l=[(1,2),(),(3,4),(),(5,6),(),(7,8)]

i=0
while i <len(l):
    if not l[i]:
        l.pop(i)
    else:
        i+=1

print("list after removing empty tuples: ",l)            