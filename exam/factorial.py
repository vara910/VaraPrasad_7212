# Factorial Calculator
# - Create a program to calculate the factorial of a number using a loop.
# - Include error handling for negative numbers.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result=1
    for i in range(1,n+1):
        result*=i
    return result
number=int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
