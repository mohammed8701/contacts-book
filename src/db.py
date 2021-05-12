import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

    
def create_db():
    """Method to create the database or not it if already exists."""
    
    sql = "CREATE DATABASE IF NOT EXISTS contactsbook;"
    cursor.execute(sql)
    connection.commit()
    

def create_table():
    
    sql = '''CREATE TABLE IF NOT EXISTS contacts (contact_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(12) NOT NULL,
    email VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    postcode VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    PRIMARY KEY(contact_id)
    );
    '''
    cursor.execute(sql)
    connection.commit()
    
def insert_contact(first,last,phone,email,address,postcode,city):
    sql = '''INSERT INTO contacts (first_name, last_name, phone_number, email, address, postcode, city) VALUES (%s,%s,%s,%s,%s,%s,%s);'''
    val = (first,last,phone,email,address,postcode,city)
    try:
        cursor.execute(sql,val)
    except Exception as e:
        print("Error: Contact not added\n",e)
    connection.commit()
    
# sort this by alphabetical ordering
def print_contacts():
    cursor.execute('SELECT * FROM contacts ORDER BY last_name ASC;')
    contact_book = cursor.fetchall()
    print("Contacts:\n")
    for contact in contact_book:
        print(f'ID: {(contact[0])}: {(contact[1])}, {contact[2]}, {contact[3]}, {contact[4]}, {contact[5]}, {contact[6]}, {contact[7]}\n')

# def select_product_by_id(product_id):
#     sql = "SELECT * FROM products WHERE product_id= %s" 
#     cursor.execute(sql,(int(product_id)))
#     connection.commit()
#     return cursor.fetchall()


def get_ids_from_db(list):
    cursor.execute('SELECT contact_id FROM contacts')
    search_terms = cursor.fetchall()
    list.clear()
    for result in search_terms:
        list.append(result[0])
    return list


def delete_contact(id):
    sql = f"DELETE FROM contacts WHERE contact_id = {item_index}"
    cursor.execute(sql)
    connection.commit()