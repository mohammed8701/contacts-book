#####


class Person:
    def __init__(self, first, last, age, phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number
        
    def full_name(self):
        print(f'{self.first} {self.last}')
        
    def __str__(self):
        return f'{self.first} {self.last}: {self.age} : {self.phone_number}'
        
contacts = list()

users_inputs = ""

print("Welcome to the Address Book")

while users_input != "q":
    print("Available options")
    print("1 - Enter a contact")
    print("2 - Display contacts")
    print("3 - Find contact")
    print("q - quit program")
    users_input = input("Select option: ")
    
    if users_input == "1":
        print("Enter your contact's information")

        first_name = input("First name = ").title()
        last_name = input("Last name = ").title()
        age = input("Age = ")
        phone_number = input("Phone number = ")

        our_contact = Person(first_name, last_name, age, phone_number)
        contacts.append(our_contact)
        print("Thank you we have received your contacts information")
        
    elif users_input == "2":
        for contact in contacts:
            print(contact)
        input("Contacts displayed. Hit enter to continue.")
        
    elif users_input == "3":
        to_lookup = input("Enter contact's name to lookup\n")
        for contact in contacts:
            if to_lookup in contact.full_name():
                print(contact)
                
    elif users_input.lower() == "q":
        break

print("Enter your contact's information?")

first_name = input("First name = ")
last_name = input("Last name = ")
age = input("Age = ")
phone_number = input("Phone number = ")

print("Thank you we have recieved your contact's information")

our_contact = Person(first_name, last_name, age, phone_number)
print(our_contact)