from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
class Child(Father):
    def disp(self):
        print("this is a childclass")
        print("it is implementing the abstract method of Father class")
class Relative(Father):pass
    # def disp(self):
    #     print("this is a relative class")
    #     print("it is implementing the abstract method of Father class") pakka a disp  func shoukd be written
c= Child()
c.disp()
r=Relative()