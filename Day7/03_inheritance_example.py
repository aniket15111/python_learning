class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_manager(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


m1=Manager("aniket",100000000,"computer science")
m1.show_employee()
m1.show_manager()