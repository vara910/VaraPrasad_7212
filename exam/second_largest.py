# Find Second Largest Number
# Write a program to find the second largest number in a list provided by the user.
def find_second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None
numbers = list(map(int, input("Enter numbers: ").split()))
second_largest = find_second_largest(numbers)
print("The second largest number is:", second_largest)
