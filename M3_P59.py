# Write a Python program to calculate the area of a trapezoid

def trapezoid_area(b1, b2, h):
    return 0.5 * (b1 + b2) * h

b1 = int(input("Enter the base1 value : "))
b2 = int(input("Enter the base2 value : "))
h= int(input("Enter the height value : "))

area = trapezoid_area(b1, b2, h)
print("The area of the trapezoid is",area)