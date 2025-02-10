import dis 
def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def get_inputs():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    return a, b, c

if __name__ == "__main__":
    num1, num2, num3 = get_inputs()
    print("The biggest number is:", find_max_of_three(num1, num2, num3))
    dis.dis(find_max_of_three)