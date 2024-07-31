from Person import Person


class CollegeEmployee(Person):

    def __init__(self):
        super().__init__()
        self.ssn = ""
        self.salary = ""
        self.department = ""

    def set_info(self):
        super().set_info()

        while True:
            self.ssn = input("Enter Social Security number (9 digits): ")
            if len(self.ssn) == 9 and self.ssn.isdigit():
                break
            print("Invalid SSN. Must be 9 digits.")

        while True:
            try:
                self.salary = float(input("Enter annual salary: "))
                break
            except ValueError:
                print("Invalid salary. Must be a number.")

        self.department = input("Enter department name: ")

    def display_info(self):
        super().display_info()
        print("SSN:", self.ssn)
        print("Salary:", self.salary)
        print("Dept:", self.department)
