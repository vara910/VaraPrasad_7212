def get_number(prompt):
    return float(input(prompt))

def add_numbers(num1, num2):
    return num1 + num2
def main():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    result = add_numbers(num1, num2)
    print("The sum of the two numbers is:", result)


if __name__ == "__main__":
    main()
    
    