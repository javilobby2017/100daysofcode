class job:
    name = None
    salary = None
    hoursWorked = None

    def __init__(self, name, salary, hoursWorked):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked
    
    def print(self):
        print("== JOB ==")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
#inheretance    
class doctor(job):
    experiance = None
    speciality = None
    
    def __init__(self, salary, hoursWorked, experiance, speciality):
        self.name = "Doctor"
        self.salary = salary
        self.hoursWorked = hoursWorked
        self.experiance = experiance
        self.speciality = speciality
    
    def print(self):
        print("== JOB ==")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
        print(f"{self.experiance:<15} {self.speciality:<15}")

class teacher(job):
    subject = None
    positions = None

    def __init__(self, salary, hoursWorked, subject, positions):
        self.name = "Teacher"
        self.salary = salary
        self.hoursWorked = hoursWorked
        self.subject = subject
        self.positions = positions
    
    def print(self):
        print("== JOB ==")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
        print(f"{self.subject:<15} {self.positions:<15}")




lawyer = job("lawyer", "100,000","40")
lawyer.print()
    
doc = doctor("$120,000", "48","7","peadeactric consultant")
doc.print()

teacher = teacher("$50,000","50","music","director")
teacher.print()

