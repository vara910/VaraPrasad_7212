# Odd and Even Separator
# - Write a program that takes a list of numbers as input and separates them into odd and
# even lists.
def odd_even_separator(numbers):
    odd_numbers=[]
    even_numbers=[]
    for number in numbers:
        if number%2==0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return odd_numbers,even_numbers
numbers=list(map(int,input("Enter the numbers: ").split()))
odd_numbers,even_numbers=odd_even_separator(numbers)
print("Odd numbers:",odd_numbers)
print("Even numbers:",even_numbers)