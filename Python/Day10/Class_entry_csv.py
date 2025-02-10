class Entry:
    def enter_details(self,name,id,age):
        with open("entry.csv","a") as file:
             file.write(f"{name},{id},{age}  \n")  
             
# file=open("entry.csv","w")              
# file.write("name, id, age\n")
# file.close()
ent=Entry()
n=int(input())
for i in range(n):
    name,id,age=input("enter name,id and age: ").split()
    ent.enter_details(name,id,age)                


