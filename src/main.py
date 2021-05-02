import os
import frequent
import menus
import db

# TO DO:
# menu options
# 1. view contacts 2. add contact 3. update contact 4. delete contact 5. search contacts


def start_app():
    
    
    print("Welcome to your Contacts Book\n")
    print('''Show Contacts: '1'
Add Contact: '2'
Update Contact: '3'
Delete Contact: '4'
Search Contact: '5'\n
Save Contacts & Exit: '0' ''')
    
    start = input("\nPlease enter one of the following options: ")
        
    show_contacts = start == "1"
    add_contacts = start == "2"
    update_contact = start == "3"
    delete_contact = start == "4"
    search_contact = start == "5"
    
    if start == '0':
        frequent.quit_app()
    
    elif show_contacts:
        frequent.clear()
        db.print_contacts()
        frequent.start_again()
    elif add_contacts:
        menus.add_contacts()
    elif update_contact:
        menus.update_contact()
    elif delete_contact:
        menus.delete_contact()
    elif search_contact:
        menus.search_contact()
        
    
def main():
    frequent.clear()
    start_app()    
    
if __name__ == "__main__":
    main()