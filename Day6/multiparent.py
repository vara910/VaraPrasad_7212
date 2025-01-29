class man:                        #parent1
    def listen(self):
        return "man can patiently listen"
class woman:                      #parent2
    def argue(self):
        return "woman always argues"
class person(man,woman):           #this is child class
    pass                           # this combines both the classes
    def dance(self):
        return "they can both dance"
obj=person()
print(obj.listen())
print(obj.argue())
print(obj.dance())
  