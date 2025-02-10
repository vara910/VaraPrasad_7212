def addition(a, b, c, d):
    return a + b + c + d

def average(a, b, c, d):
    total = addition(a, b, c, d)
    return total / 4

def get_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    return num1, num2, num3, num4

def display(average):
    print(f"The average of the four numbers is: {average}")

def main():
    num1, num2, num3, num4 = get_numbers()
    avg = average(num1, num2, num3, num4)
    display(avg)

if __name__ == "__main__":
    main()