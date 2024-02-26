#Write a Python function that takes two lists and returns true if they have at least one common member
def have_common_member(list1, list2):

    set1 = set(list1)
    set2 = set(list2)
    
    return bool(set1.intersection(set2))

list1 = [1, 2, 3, 4, 5]
list2 = [10, 6, 7, 8, 9]
print(have_common_member(list1, list2))  