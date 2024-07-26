from Person import Person


class CollegeEmployee(Person):

    def __init__(self):
        super().__init__()
        self.ssn = ""
        self.salary = ""
        self.department = ""

    def set_info(self):
        super().set_info()
        # TODO: Add character limit and type checking for SSN
        self.ssn = input("Enter Social Security number: ")
        # TODO: Add type checking for salary
        # Regular code comment for example 
        self.salary = float(input("Enter annual salary: "))
        self.department = input("Enter department name: ")

    def display_info(self):
        super().display_info()
        print(f"SSN: {self.ssn}, Salary: {self.salary}, Dept: {self.department}")
