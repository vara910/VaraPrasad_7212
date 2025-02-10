class parent:
    def __init__(self):
        self.bigNose="7cm"
    def display_parent(self):
        print("this is the parent class")
class Child(parent):
    def __init__(self):
        super().__init__()
    def display_child(self):
        print("this is the child class")
child=Child()
child.display_child()
child.display_parent()
print(child.bigNose)