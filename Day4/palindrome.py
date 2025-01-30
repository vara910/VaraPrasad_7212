<<<<<<< HEAD
def display(ans):
    if(ans):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
def isPalindrome(lst):
    if(lst==lst[::-1]):
        return True
    else:
        return False
def main():
    string=input("Enter the input: ")
    lst=list(string)
    ans=isPalindrome(lst)
    display(ans)
=======
def display(ans):
    if(ans):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
def isPalindrome(lst):
    if(lst==lst[::-1]):
        return True
    else:
        return False
def main():
    string=input("Enter the input: ")
    lst=list(string)
    ans=isPalindrome(lst)
    display(ans)
>>>>>>> 358754402b0669febcc8430179e2723405681dd5
main()