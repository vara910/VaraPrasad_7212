class Example:
    def __init__(self, name=None, age=None):
        if name is not None:
            print(f"first constructor: hELLO {name}")
        if age is not None:
            print(f"second Constructor: age is {age}")
obj1 = Example(age=25)

class Example2:
    def __init__(self,*args):
        if len(args)==1:
            print(f"hello {args[0]}")
        elif len(args)==2:
            print(f"hello {args[0]}, you are {args[1]} years old")
obj2=Example2("vara")

class Example3:
    def __init__(self,**kwargs):
        if "name" in kwargs and "age" in kwargs:
            print(f"hello {kwargs['name']},you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"hello {kwargs['name']}")
obj3=Example3(name="vara")
obj4=Example3(name="vara",age=30)
#print(obj3.studentname)
