#Write a Python function to check whether a number is in a given range.

def in_range():
    
    start = int(input("Enter the start value : "))
    end = int(input("Enter the end value : "))
    
    n = int(input("Enter a value : "))
    
    if start<= n <= end :
        print(n,"Number is in the given range. ")
    
    else :
            print(n,"is not in range.")
            
in_range()