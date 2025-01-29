class Example:
    static_var = 0  # This is a static variable

    def __init__(self, value):
        self.value = value
        Example.static_var += 1

    def display(self):
        print(f"Value: {self.value}, Static Variable: {Example.static_var}")

# Create instances of the class
obj1 = Example(10)
obj1.display()

obj2 = Example(20)
obj2.display()

obj3 = Example(30)
obj3.display()