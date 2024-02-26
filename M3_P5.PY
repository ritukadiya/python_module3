#How will you compare two lists? 
def compare(l1,l2):
    l1.sort()
    l2.sort()

    if l1==l2:
        return "equal"
    else:
        return "non equal"
l1=[1,2,3]
l2=[2,1,3]
print("first comparision : ",compare(l1,l2))

l3=[1,2,3]
l4=[1,4,3]
print("second comparision : ",compare(l3,l4))