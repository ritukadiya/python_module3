# Write a Python program to reverse a tuple.
def rev_tuple(t):
    rev_tuple=t[::-1]
    return rev_tuple

my_tuple=(1,2,3,4,5)
rev_tuple=rev_tuple(my_tuple)
print("reversed tuple:",rev_tuple)