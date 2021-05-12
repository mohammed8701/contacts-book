import pymysql
import os
# from dotenv import load_dotenv
import csv
# from prettytable import from_csv
import frequent
import db

def new_contact_first_name():
    while True:
        
        contact_first_name_input = input("\nPlease enter the first name of the contact: \n").title()
        if contact_first_name_input != '':
            return contact_first_name_input
            False
        else:
            print('\nSorry, you need to enter a valid first name.\n')
        
        # frequent.print_invalid_option()

def new_contact_last_name():
    while True:
        contact_last_name_input = input("\nPlease enter the last name of the contact:\n").title()
        if contact_last_name_input != '':
            return contact_last_name_input
            False
        else:
            print('\nSorry, you need to enter a valid last name.\n')
            
            
def new_contact_number():
    while True:
        contact_phone_number_input = int(input("\nPlease enter the phone number of the contact:\n").title())
        if contact_phone_number_input != '' or len(contact_phone_number_input) <= 11:
            return str(contact_phone_number_input)
            False
        else:
            print('\nSorry, you need to enter a valid phone number.\n')

def new_contact_email():
    while True:
        contact_email_input = input("\nPlease enter the email address of the contact:\n")
        if "@"  in contact_email_input:
            return contact_email_input
            False
        else:
            print('\nSorry, you need to enter a valid email address.\n')

def new_contact_address():
    while True:
        contact_address_input = input("\nPlease enter the address of the contact without postcode:\n").title()
        if contact_address_input != '':
            return contact_address_input
            False
        else:
            print('\nSorry, you need to enter a valid address.\n')
            
def new_contact_postcode():
    while True:
        contact_postcode_input = input("\nPlease enter the post code of the contact without postcode:\n").upper()
        if contact_postcode_input != '':
            return contact_postcode_input
            False
        else:
            print('\nSorry, you need to enter a valid post code.\n')            

def new_contact_city():
    while True:
        contact_city_input = input("\nPlease enter the city of the contact without postcode:\n").title()
        if contact_city_input != '':
            return contact_city_input
            False
        else:
            print('\nSorry, you need to enter a valid city.\n') 

# function to show all your current stored contacts
def add_contacts():
    first_name = new_contact_first_name()
    last_name = new_contact_last_name()
    phone_number = new_contact_number()
    email = new_contact_email()
    address = new_contact_address()
    post_code = new_contact_postcode()
    city = new_contact_city()
    
    db.insert_contact(first_name,last_name,phone_number,email,address,post_code,city)
    frequent.clear()
    print("Contact Added!")
    frequent.start_again()

contact_id_list = []
def index_selector():
    id_list = db.get_ids_from_db(contact_id_list)
    while True:
        contact_to_select_index = input("\nPlease select the index of the contact you wish to delete\n")
        
        if contact_to_select_index != "0" and int(contact_to_select_index) in contact_id_list:
            return(int(contact_to_select_index))
            False
        
        else:
            frequent.clear()
            print("Error: Please select a contact from the list")

def delete_contact():
    db.print_contacts()
    id_to_delete = index_selector()
    try:
        db.delete_contact(id_to_delete)
        print("Contact Deleted")
        frequent.start_again()
        
    except Exception as e:
        print("Error:", e) 
    
