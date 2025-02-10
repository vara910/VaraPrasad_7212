class Cat:
    def sound(self):
        print("meow")
class Dog:
    def sound(self):
        print("bark")
class Horse:
    def sound(self):
        print("neigh")
for animal in [Cat(),Dog(),Horse()]:
    animal.sound()

