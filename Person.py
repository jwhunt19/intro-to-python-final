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
        while True:
            self.phone = input("Enter phone number: ")
            if self.phone.isdigit() and len(self.phone) == 10:
                break
            print("Invalid phone number. Must be 10 digits.")

    def display_info(self):
        print("Name: ", self.first_name, self.last_name)
        print("Address: ", self.address, self.zipcode)
        print("Phone: ", self.phone)
