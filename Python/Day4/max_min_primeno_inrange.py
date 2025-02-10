def display(minn,maxx):
    print(f"The smallest prime number in the range is: {minn}")
    print(f"The largest prime number in the range is: {maxx}")
def max_min(lst):       #finding in single function
    maxx=float("-inf")
    minn=float("inf")
    for i in lst:
        if(i>=maxx):
            maxx=i
        if(i<=minn):
            minn=i
    return minn,maxx
def check_prime(n):
    if(n>=2):
        for i in range(2,int(n**(0.5))+1):
            if(n%i==0):
                return False
        return True
    else:
        return False
def main():
    a=int(input("Enter initial range: "))
    b=int(input("Enter final range: "))
    lst=[]
    if(a<b and a>0 and b>0):
        for i in range(a,b+1):
            if(check_prime(i)):
                lst.append(i)
        minn,maxx=max_min(lst) #finding in single function
        display(minn,maxx)
    else:
        print("the first input should be smaller than second input")

    
    
    
main()