# Empty list
l1=[]
print("The empty list is: ",l1)

#List with elements
l2=[1,2,3,4]
print(" l2 list with elements: ",l2)

# accessing a element by index
print("3rd elemnts in list at index l2[2] is: ",l2[2])

#nested list
l3=[1,[1,2],[1,2,3]]
print("Nested List l3: ",l3)

#accessing nested list
print("Element at l3[1]:",l3[1])
print("element at index l3[1][1]:",l3[1][1])
print("Slicing a sublist of l3[2][1:3]",l3[2][1:3])

#creating a list from string
l4=list("hello")
print("Creating a l4 list from string hello: ",l4)

#hetrogeneous list
l5=[1,"hello",30,"hi"]
print("Hetrogeneous list l5: ",l5)

#getting length of list
l6=[1,2,3,5,6]
print("Length of list l6 is:",l6,len(l6))

#list created from ranges
l7=list(range(-9,9))
print("List l7 created from ranges -9 to 9: ",l7)

#slicing of list
print("The slicing from list l7 from index 3 to 7 is l7[3:7]",l7[3:7])


##adding elements into list using for loop
def array_Elements(n):
    arr=[]
    for i in range(n):
        m=int(input())
        arr[i]=m
    return arr
def main():
    n=int(input("Enter size of array: "))
    ans=array_Elements(n)
    print(*ans)
main()

#membership
print("3 in [1,2,3]", 3 in [1,2,3])