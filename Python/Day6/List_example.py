class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def set_salary(self, salary):
        self.salary = salary

    def __repr__(self):
        return f"{self.name} earns {self.salary}"

emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)
ls = [emp1, emp2]

print(ls)
print(ls[0].name)  # Output: John
print(ls[1].salary)  # Output: 60000