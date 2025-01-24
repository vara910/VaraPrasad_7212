import dis
def multiply(a, b):
    return a * b
def main():
    n = int(input("Enter the number of iterations: "))
    for _ in range(n):
        num1 = int(input("Enter the first number: ")) 
        num2 = int(input("Enter the second number: "))
        result = multiply(num1, num2)
        print(f"The multiplication is {result}")
    dis.dis(multiply)
    dis.dis(main)
if __name__ == "__main__":
    main()
