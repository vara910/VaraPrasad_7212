def convert_into_lst(n):
    lst=[]
    s=""
    for i in n:
        if(i!=" "):
            s+=i
        else:
            if(s!=""):
                lst.append(s)
                s=""
    if(s!=""):
        lst.append(s)
    return lst
def display(i,ans):
    if(ans):
        print(f"{i} - is a palindrome")
    else:
        print(f"{i} - is not a palindrome")
def isPalindrome(lst):
    if(lst==lst[::-1]):
        return True
    else:
        return False
def main():
    n=input("Enter the string or sentence:\n")
    lst=convert_into_lst(n)
    for i in lst:
        ans=isPalindrome(i)
        display(i,ans)
main()