from Person import Person


class Student(Person):
    def __init__(self):
        super().__init__()
        self.major = ""
        self.gpa = 0.0

    def set_info(self):
        super().set_info()
        self.major = input("Enter major: ")
        while True:
            try:
                self.gpa = float(input("Enter GPA: "))
                break
            except ValueError:
                print("Invalid GPA. Must be a number.")

    def display_info(self):
        super().display_info()
        print("Major: ", self.major)
        print("GPA: ", self.gpa)
