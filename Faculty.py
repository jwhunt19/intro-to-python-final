from CollegeEmployee import CollegeEmployee


class Faculty(CollegeEmployee):
    def __init__(self):
        super().__init__()
        self.tenured = False

    def set_info(self):
        super().set_info()

        while True:
            tenured_input = input("Tenured? (y/n): ").lower()
            if tenured_input == "y":
                self.tenured = True
                break
            elif tenured_input == "n":
                self.tenured = False
                break
            else:
                print("Invalid input. Enter y or n.")

    def display_info(self):
        super().display_info()
        print(f"Tenured: {self.tenured}")
