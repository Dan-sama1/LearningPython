def menu():
    print('--------------------')
    print("----- CONTACTS -----")
    print('--------------------')
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")


def add_contacts(contacts):
    print("----- ADD A CONTACT -----")
    try:
        name = input("Enter name: ")
        phone_num = input("Enter phone number: ")
        if not phone_num.isdigit():
            raise ValueError("Phone number should be digits only.")
        email_add = input("Enter email: ")
        contacts[name] = {"Phone:": phone_num, "Email:": email_add}
        print(f'{name} Added to the contacts.')
        input("Press any key to continue...")
    except ValueError:
        print("Please enter a valid phone number.")
        add_contacts(contacts)


def view_contacts(contacts):
    print("----- VIEW CONTACTS -----")
    for name, info in contacts.items():
        print(f'Name: {name} | Phone: {info["Phone:"]} | Email: {info["Email:"]}')


def update_contacts(contacts):
    print("----- UPDATE CONTACT -----")
    while True:
        print("Enter the name of the contact [x to EXIT]:")
        name = input(">> ")
        if name.lower() == "x":
            break
        if name in contacts:
            while True:
                print("1. Update name")
                print("2. Update phone number")
                print("3. Update Email")
                print("4. Exit")
                choice = int(input(">> "))
                if choice == 1:
                    new_name = input("Enter new name: ")
                    contacts[new_name] = contacts.pop(name)
                    name = new_name
                elif choice == 2:
                    phone_num = input("Enter new phone number: ")
                    if not phone_num.isdigit():
                        print("Phone number should be digits only.")
                    else:
                        contacts[name]["Phone:"] = phone_num
                elif choice == 3:
                    email_add = input("Enter new Email: ")
                    contacts[name]["Email:"] = email_add
                elif choice == 4:
                    return
                else:
                    print("Invalid choice please try again.")

                print("Contact updated.")
                input("Press any key to continue...")
        else:
            print("Contact not found :(")
            input("Press any key to continue...")


def delete_contact(contacts):
    print("Enter name: ")
    name = input(">> ")
    if name in contacts:
        print(f'Name: {name} | Phone: {contacts[name]["Phone:"]} | Email: {contacts[name]["Email:"]}')
        print()
        print("ARE YOU SURE YOU WANT TO DELETE THIS CONTACT? [Y/N]")
        while True:
            choice = input(">> ").upper()
            if choice == 'Y':
                del contacts[name]
                print("Contact Deleted Successfully.")
                input("Press any key to continue...")
                break
            elif choice == 'N':
                print("Contact Deletion cancelled.")
                input("Press any key to continue...")
                break
            else:
                print("Invalid input, please try again.")


def main():
    contacts = {}
    while True:
        menu()
        print("Enter your choice:")
        try:
            choice = int(input(">> "))
            if choice == 1:
                add_contacts(contacts)
            elif choice == 2:
                view_contacts(contacts)
            elif choice == 3:
                update_contacts(contacts)
            elif choice == 4:
                delete_contact(contacts)
            elif choice == 5:
                input("Press ANY key to EXIT...")
                break
            else:
                print("Invalid choice, please try again...")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
