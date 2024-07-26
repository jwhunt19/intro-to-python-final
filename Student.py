from Person import Person


class Student(Person):
    def __init__(self):
        super().__init__()
        self.major = ""
        self.gpa = 0.0

    def set_info(self):
        super().set_info()
        self.major = input("Enter major: ")
        # TODO: Add type checking for GPA
        self.gpa = float(input("Enter GPA: "))

    def display_info(self):
        super().display_info()
        print(f"Major: {self.major}, GPA: {self.gpa}")
