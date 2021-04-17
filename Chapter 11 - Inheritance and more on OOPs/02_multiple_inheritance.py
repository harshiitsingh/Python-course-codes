class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Harshit"

p = Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.name)
print(p.company)  # here visa will be printed coz Employee is written first [inside Programmer(Employee, Freelancer)]