# #Palindrome Checker
# - Write a program to check if a given string or number is a palindrome.
# - Allow the user to input multiple values using a loop.
def palindrome_checker(value):
    value=str(value)
    return value==value[::-1]
if __name__=="__main__":
    while True:
        value=input("Enter a value: ")
        if palindrome_checker(value):
            print(f"{value} is a palindrome.")
        else:
            print(f"{value} is not a palindrome.")
        choice=input("Do you want to continue? (y/n): ")
        if choice.lower()!="y":   
            break