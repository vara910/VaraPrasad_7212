<<<<<<< HEAD
def summ(ele):
    sm=0
    for i in ele:
        sm+=i
    return sm
def reading_elements(n):
    lst=[]
    for i in range(n):
        m=int(input())
        lst.append(m)
    return lst
def main():
    n=int(input("Enter the number of elements: "))
    elements=reading_elements(n)
    ans=summ(elements)
    print(f"Sum of elements of length {n} is: ",ans)
    print("approch 2 is inbuilt function sum()->sum(elements):" ,sum(elements))
=======
def summ(ele):
    sm=0
    for i in ele:
        sm+=i
    return sm
def reading_elements(n):
    lst=[]
    for i in range(n):
        m=int(input())
        lst.append(m)
    return lst
def main():
    n=int(input("Enter the number of elements: "))
    elements=reading_elements(n)
    ans=summ(elements)
    print(f"Sum of elements of length {n} is: ",ans)
    print("approch 2 is inbuilt function sum()->sum(elements):" ,sum(elements))
>>>>>>> 358754402b0669febcc8430179e2723405681dd5
main()