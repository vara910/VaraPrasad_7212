from abc import ABC, abstractmethod
from typing import List

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass
    
    @abstractmethod
    def working_hours(self) -> int:
        pass


# Step 2: Create concrete classes for different types of employees

class Manager(Employee):
    def __init__(self, name: str, salary: float ,hourss:int):
        self.name = name
        self.salary = salary
        self.hourss= hourss

    def work(self) -> str:
        return f"{self.name} is managing the team."

    def get_salary(self) -> float:
        return self.salary
    
    def working_hours(self) -> int:
        return self.hourss
    


class Developer(Employee):
    def __init__(self, name: str, salary: float ,hourss:int):
        self.name = name
        self.salary = salary
        self.hourss= hourss

    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary
    
    def working_hours(self) -> int:
        return self.hourss


class Intern(Employee):
    def __init__(self, name: str, salary: float ,hourss:int):
        self.name = name
        self.salary = salary
        self.hourss= hourss

    def work(self) -> str:
        return f"{self.name} is learning and assisting."

    def get_salary(self) -> float:
        return self.salary
    
    def working_hours(self) -> int:
        return self.hourss


# Step 3: Define Department class that manages Employees

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")

    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")

    def promote(self,employee: Employee) -> None:
            if employee.name=="Alice" and employee.hourss>35:
                print(f"{employee.name} has been promted to senior manager")
            if employee.name=="Bob" and employee.working_hours>80:
                print(f"{employee.name} has been promted to assistant manager")
            if employee.name=="Charlie" and employee.working_hours>50:
                print(f"{employee.name} has been promted to developerr")
            if employee.name=="Ram" and employee.working_hours>84:
                print(f"{employee.name} has been promted to head of security")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: {employee.get_salary()},working_hours:{employee.working_hours()} Role: {employee.work()} ")

class Security(Employee):
    def __init__(self, name: str, salary: float ,hourss:int):
        self.name = name
        self.salary = salary
        self.hourss= hourss

    def work(self) -> str:
        return f"{self.name} is Securing the assets."

    def get_salary(self) -> float:
        return self.salary
    
    def working_hours(self) -> int:
        return f"{self.hourss}"
    
# Step 4: Create department and add employees

# Create employees
manager = Manager("Alice", 80000 ,25)
developer = Developer("Bob", 60000 ,20)
intern = Intern("Charlie", 20000 ,30)
securitystaff=Security("Ram",5000 ,15)

# Create a department and hire employees
it_department = Department("IT")

it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(securitystaff)
# Show employee details
it_department.show_employee_details()
it_department.promote(manager)

# Total salary in the department
total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")