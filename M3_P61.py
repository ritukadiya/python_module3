# Write a Python program to calculate surface volume and area of a cylinder

import math 

def cylinder_surface(r,h):
    
    surface =2*math.pi*r*(r+ h)
    print("Cylinder surface is : ",surface)
    
def cylinder_area(r,h) :
    
    area = math.pi*r** 2 * h
    print("Cylinder area is : ",area)
    
r=int(input("Enter the cylinder radius : "))
h=int(input("Enter the cylinder height : "))
cylinder_surface(r,h)
cylinder_area(r,h)