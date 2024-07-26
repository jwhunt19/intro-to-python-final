from CollegeEmployee import CollegeEmployee


class Faculty(CollegeEmployee):
    def __init__(self):
        super().__init__()
        self.tenured = False

    def set_info(self):
        super().set_info()
        # TODO: Add type checking for tenured
        self.tenured = input("Tenured (y/n)? ").lower() == "y"

    def display_info(self):
        super().display_info()
        print(f"Tenured: {self.tenured}")
