
class Employee:
    company = "Google"

    def __init__(self):
        # super().__init__()
        print("Employee is created.")

    def getSalary(self, signature): 
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry = Employee()

