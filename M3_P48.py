# Write a Python function to calculate the factorial of a number (a nonnegative integer)

n=int(input("Enter a non-negative integer : "))

if n<0:
    print("Please enter a non-negative integer.")
else:
    result = 1
    for i in range(1,n+1):
        result =result*i

    print("The factorial of ",n," is:" ,result)