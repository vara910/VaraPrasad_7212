def display(minn,maxx):
    print(f"The minimum number in the list is: {minn}")
    print(f"The maximum number in the list is: {maxx}")
def find_max(ele):
    maxx=float("-inf")
    for i in ele:
        if(i>=maxx):
            maxx=i
    return maxx
def find_min(ele):
    minn=float("inf")
    for i in ele:
        if(i<=minn):
            minn=i
    return minn

def max_min(lst):       #finding in single function
    maxx=float("-inf")
    minn=float("inf")
    for i in lst:
        if(i>=maxx):
            maxx=i
        if(i<=minn):
            minn=i
    return minn,maxx
def reading_elements(n):
    lst=[]
    for i in range(n):
        m=int(input(f"enter {i+1} element: "))
        lst.append(m)
    return lst
def main():
    n=int(input("Enter the number of elements: "))
    elements=reading_elements(n)
    minn=find_min(elements)
    maxx=find_max(elements)
    min2,max2=max_min(elements) #finding in single function
    
    display(minn,maxx)
    display(min2,max2)
main()