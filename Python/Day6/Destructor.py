class Destructor:
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} is created")
    def __del__(self):
        print(f"object {self.name} is destroyed")
obj=Destructor("vara")
del obj