file=open("example_csv.csv","a")
file.write("name, id, age\n")
with open("example_csv.csv","a") as file:
    n=int(input())
    for i in range(n):
        name,id,age=input("enter name id and age").split()
        file.write(f"{name},{id},{age}:`    \n")