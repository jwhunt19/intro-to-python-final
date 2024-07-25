class Person:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.address = ""
        self.zipcode = ""
        self.phone = ""

    def set_info(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.address = input("Enter street address: ")
        self.zipcode = input("Enter zip code: ")
        self.phone = input("Enter phone number: ")

    def display_info(self):
        print(
            f"Name: {self.first_name} {self.last_name} \nAddress: {self.address} {self.zipcode} \nPhone: {self.phone}"
        )
