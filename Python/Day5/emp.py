class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
        self._food = 0
        self._travel = 0
        self._gst = 0

    def allowance(self, food, travel):
        self._food = food
        self._travel = travel
        return self._food + self._travel

    def get_allowance(self):
        return self._food + self._travel

    def deduction(self, gst):
        self._gst = gst
        return self._gst

    def get_deduction(self):
        return self._gst

    def calculate_net_salary(self):
        return self.base_salary + self.get_allowance() - self.get_deduction()

emp = Employee("John Doe", 50000)
print("Allowance:", emp.allowance(5000, 2000))
print("Allowance:", emp.get_allowance())
print("Deduction:", emp.deduction(3000))
print("Net Salary:", emp.calculate_net_salary())
