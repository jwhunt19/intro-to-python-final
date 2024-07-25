from Person import Person

class CollegeEmployee(Person):

    def __init__(self):
        super().__init__()
        self.ssn = ""
        self.salary = ""
        self.department = ""

    def set_info(self):
        super().set_info()
        self.ssn = input("Enter Social Security number: ")
        self.salary = float(input("Enter annual salary: "))
        self.department = input("Enter department name: ")

    def display_info(self):
        super().display_info()
        print(f", SSN: {self.ssn}, Salary: {self.salary}, Dept: {self.department}")
    