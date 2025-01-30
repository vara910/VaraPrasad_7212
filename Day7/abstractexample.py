from abc import ABC,abstractmethod
class Father(ABC):
    def display(self):
        pass
    def show(self):
        print("concrete method is this only")
class Son(Father):
    def display(self):
        print("son is implementing the astract method")
class Daughter(Father):
    def display(self):
        print("daughter is also implementing the abstract class")
        
s =Son()
s.display()
s.show()
d=Daughter()
d.display()
d.show()
