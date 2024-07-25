from Person import Person

class Student(Person):
    def __init__(self):
        super().__init__()
        self.major = ""
        self.gpa = 0.0
    
    def set_info(self):
        super().set_info()
        self.major = input("Enter major: ")
        self.gpa = float(input("Enter GPA: "))