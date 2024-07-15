import os
def menu():
    print('--------------------')
    print("----- CONTACTS -----")
    print('--------------------')
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")


def add_contacts():
    try:
        print("----- ADD A CONTACT -----")
        name = input("Enter name: ")
        phone_num = input("Enter phone number: ")
        if not phone_num.isdigit():
            raise ValueError("Phone number should be digits only.")
        email_add = input("Enter email: ")

        with open("D:\\DAN\\PATH\\CONTACTS.txt", 'a+') as file:
            file.seek(0)
            contacts = file.readlines()
            contact = f"Name: {name} | Phone: {phone_num} | Email: {email_add}\n"
            if contact in contacts:
                print("Contact already exists...")
            else:
                file.write(contact)
                print("Contact added successfully.")
    except ValueError as e:
        print(e)
        add_contacts()


def view_contacts():
    print("----- VIEW CONTACTS -----")
    with open("D:\\DAN\\PATH\\CONTACTS.txt", 'r') as file:
        contacts = file.readlines()
        if contacts:
            for i in contacts:
                print(i.strip())
        else:
            print("No contact found.")
    input("Press ANY key to continue...")


def update_contacts():
    print("----- UPDATE CONTACT -----")
    with open("D:\\DAN\\PATH\\CONTACTS.txt", 'r') as file:
        contacts = file.readlines()
    contact_found = False
    print("Enter Contact name: ")
    name = input(">> ")

    for index, contact in enumerate(contacts):
        parts = contact.strip().split(" | ")
        contact_name = parts[0].split(": ")[1]

        if contact_name == name:
            contact_found = True
            print(f"Contact found: {contact.strip()}")
            while True:
                print("1. Update name")
                print("2. Update phone number")
                print("3. Update Email")
                print("4. Exit")
                try:
                    choice = int(input(">> "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")
                    continue
                if choice == 1:
                    new_name = input("Enter new name: ")
                    parts = contact.split(" | ")
                    parts[0] = f"Name: {new_name}"
                    print("Name Updated Successfully.")
                elif choice == 2:
                    new_phone_num = input("Enter new phone number: ").strip()
                    if not new_phone_num.isdigit():
                        print("Phone number should be digits only.")
                        continue
                    parts[1] = f"Phone: {new_phone_num}"
                    print("Phone number updated successfully.")
                elif choice == 3:
                    new_email_add = input("Enter new email: ").strip()
                    parts[2] = f"Email: {new_email_add}"
                    print("Email updated successfully.")
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")

                contacts[index] = " | ".join(parts) + "\n"
            break

    if not contact_found:
        print("Contact not found")

    with open("D:\\DAN\\PATH\\CONTACTS.txt", 'w') as file:
        file.writelines(contacts)

    input("Press ANY key to continue")


def delete_contacts():
    print("----- DELETE CONTACT -----")
    name = input("Enter contact name: ").strip()
    with open("D:\\DAN\\PATH\\CONTACTS.txt", 'r') as file:
        contacts = file.readlines()

    found = False
    with open("D:\\DAN\\PATH\\CONTACTS.txt", 'w') as file:
        for contact in contacts:
            if f"Name: {name} " in contact:
                while True:
                    print(f"Are you sure you want to delete this contact?\n{contact.strip()} [Y/N]")
                    choice = input(">> ").strip().upper()
                    if choice == 'Y':
                        print("Contact deleted successfully.")
                        found = True
                        break
                    elif choice == 'N':
                        print("Contact deletion cancelled.")
                        file.write(contact)
                        found = True
                        break
                    else:
                        print("Invalid input, please try again.")
            else:
                file.write(contact)
    if not found:
        print("Contact not Existing.")
    else:
        input("Press ANY key to continue")


def main():
    while True:
        menu()
        try:
            print("Enter choice:")
            choice = int(input(">> "))
            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid choice, please try again.")
            if choice == 1:
                add_contacts()
            elif choice == 2:
                view_contacts()
            elif choice == 3:
                update_contacts()
            elif choice == 4:
                delete_contacts()
            elif choice == 5:
                print("Thank you for using.")
                input("Press ANY key to exit...")
                break
        except ValueError:
            print("Invalid choice please try again")


if __name__ == '__main__':
    main()
