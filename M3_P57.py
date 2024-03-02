#Write a Python program to read a random line from a file.
import random

def read_random_line():
    file = open("test.txt","r")
    print(file.readlines())
    
    file.close
    

read_random_line()