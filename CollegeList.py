from CollegeEmployee import CollegeEmployee
from Faculty import Faculty
from Student import Student


def main():
    print("Which type of person's data will you be entering?")
    print("C: College employee, F: Faculty, S: Student, Q: Quit")

    college_employees = []
    faculty = []
    students = []

    data_limit_dict = {"C": 4, "F": 3, "S": 7}

    while True:
        choice = input("Enter C, F, S, or Q: ").upper()

        match choice:
            case "C":
                if len(college_employees) == data_limit_dict[choice]:
                    print("You have reached the maximum number of college employees.")
                    continue
                c = CollegeEmployee()
                c.set_info()
                college_employees.append(c)
            case "F":
                if len(faculty) == data_limit_dict[choice]:
                    print("You have reached the maximum number of faculty.")
                    continue
                f = Faculty()
                f.set_info()
                faculty.append(f)
            case "S":
                if len(students) == data_limit_dict[choice]:
                    print("You have reached the maximum number of students.")
                    continue
                s = Student()
                s.set_info()
                students.append(s)
            case "Q":
                break
            case _:
                print("Invalid choice")
                continue

    print("\nCollege Employees")
    print("=================")
    if len(college_employees) == 0:
        print("No college employees entered.")
    else:
        for c in college_employees:
            c.display_info()
            print("")

    print("Faculty")
    print("=================")
    if len(faculty) == 0:
        print("No faculty entered.")
    else:
        for f in faculty:
            f.display_info()
            print("")

    print("Students")
    print("=================")
    if len(students) == 0:
        print("No students entered.")
    else:
        for s in students:
            s.display_info()
            print("")


main()
