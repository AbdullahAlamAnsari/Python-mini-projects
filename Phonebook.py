
phone_book = {}

def add_contact():
    name = input("Enter Name: ").title()
    print(name)
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    if name in phone_book:
        print(f"{name} already exists. Use update option.")
    else:
        phone_book[name] = (phone, email)
        print(f"{name} added successfully!")

def update_contact():
    name = input("Enter Name to update: ")
    if name in phone_book:
        phone = input("Enter new Phone Number: ")
        email = input("Enter new Email: ")
        phone_book[name] = (phone, email)
        print(f"{name} updated successfully!")
    else:
        print(f"{name} does not exist!")

def delete_contact():
    name = input("Enter Name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"{name} deleted successfully!")
    else:
        print(f"{name} does not exist!")

def search_contact():
    name = input("Enter Name to search: ")
    if name in phone_book:
        phone, email = phone_book[name]
        print(f"Name: {name}, Phone: {phone}, Email: {email}")
    else:
        print(f"{name} not found!")

def display_contacts():
    if not phone_book:
        print("Phone book is empty.")
    else:
        print("All Contacts:")
        for name, (phone, email) in phone_book.items():
            print(f"Name: {name}, Phone: {phone}, Email: {email}")

# Main program loop
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

# Run the program
phone_book_menu()
