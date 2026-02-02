phone_book = {}

def add_contact():
    name = input("Enter the name to be added: ")
    email = input("Enter the mail to be added: ")
    phonenumber = input("Enter the phone number to be added: ")
    if name in phone_book:
        print("USER NAME ALREADY EXISTS!")
    elif name not in phone_book:
        phone_book[name] = (email,phonenumber)
        print(f"{name} information successfully added with phone number {phonenumber} and email {email}")

def update_contact():
    name = input("Enter your username: ")
    if name in phone_book:
            phonenumber = input("Enter the number: ")
            email = input("Enter new email: ")
            phone_book[name] = (email,name)

def delete_contact():
    name = input("Enter the name of the user whose data you  want to delete: ")
    if name in phone_book:
        del phone_book[name]
        print("USER CONTACT DELETED SUCCESSFULLY!")

def search_contact():
    name = input("Enter the name of the user: ")
    if name in phone_book:
        email,phone = phone_book[name]
        print(f"NAME: {name}\nEMAIL: {email}\nPHONE NUMBER: {phone}")
        
def display_contacts():
    for names in phone_book:
        email,phone = phone_book[names]
        print(f"NAME: {names}\nEMAIL: {email}\nPHONE NUMBER: {phone}")
        
            
def phone_book_menu():
    while True:
        print("\n--- Phone Book Menu ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("Exiting Phone Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-6.")

phone_book_menu()