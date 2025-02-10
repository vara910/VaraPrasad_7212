def fibonacci(n1,n2,max_nos):

    lst=[]
    lst.append(n1)
    lst.append(n2)
    for i in range(3,max_nos+1):
        new_num=lst[-1]+lst[-2]
        lst.append(new_num)
    return lst
def main():
    n1=-1
    n2=0
    maxNumbers=int(input("Enter how many number do you want: "))
    ans=fibonacci(n1,n2,maxNumbers)
    print(*ans)
main()