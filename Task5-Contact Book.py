# CONTACT BOOK - OPTIMIZED VERSION

contacts = {}

while True:

    print("\n===== CONTACT BOOK =====")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD CONTACT

    if choice == "1":

        name = input("Enter Name: ")

        phone = input("Enter Phone: ")

        email = input("Enter Email: ")

        address = input("Enter Address: ")

        contacts[name] = [phone, email, address]

        print("Contact added successfully!")

    # VIEW CONTACTS

    elif choice == "2":

        if not contacts:

            print("No contacts available.")

        else:

            print("\n===== CONTACT LIST =====")

            for name, details in contacts.items():

                print("\nName:", name)

                print("Phone:", details[0])

                print("Email:", details[1])

                print("Address:", details[2])

    # SEARCH CONTACT

    elif choice == "3":

        search = input("Enter Name or Phone: ")

        found = False

        for name, details in contacts.items():

            if search == name or search == details[0]:

                print("\nContact Found")

                print("Name:", name)

                print("Phone:", details[0])

                print("Email:", details[1])

                print("Address:", details[2])

                found = True

        if not found:

            print("Contact not found.")

    # UPDATE CONTACT

    elif choice == "4":

        name = input("Enter contact name to update: ")

        if name in contacts:

            phone = input("Enter new phone: ")

            email = input("Enter new email: ")

            address = input("Enter new address: ")

            contacts[name] = [phone, email, address]

            print("Contact updated successfully!")

        else:

            print("Contact not found.")

    # DELETE CONTACT

    elif choice == "5":

        name = input("Enter contact name to delete: ")

        if name in contacts:

            del contacts[name]

            print("Contact deleted successfully!")

        else:

            print("Contact not found.")

    # EXIT

    elif choice == "6":

        print("Thank you for using Contact Book!")

        break

    # INVALID CHOICE

    else:

        print("Invalid choice. Please try again.")