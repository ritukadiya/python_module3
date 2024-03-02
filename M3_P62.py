#Write a Python program to returns sum of all divisors of a number
def sum_of_divisors():
    
    n= int(input("Enter the number : "))
    divisor_sum = 0
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            
            if i != n // i:
                divisor_sum += n // i
                
    print("Sum of divisors is : ",divisor_sum)

sum_of_divisors()