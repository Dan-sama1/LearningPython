
def home():
    print("="*32)
    print("Create account [C], Log in [L], Delete account [D] or Exit System [EXIT]")
    choose = str(input(">>").upper())
    print("=" * 32)
    if choose not in ['C', 'L', 'D', 'EXIT']:
        print(">> Invalid, Please try again")
        return None
    return choose

def create_acc():
    print('='*8 + ' CREATE ACCOUNT ' + '='*8)
    loop = True
    while loop:
        em = input("Enter Email: ")
        pw = input("Enter password: ")
        confirm_pw = input("Confirm password: ")
        if pw == confirm_pw:
            with open("D:\\DAN\\PATH\\ACCOUNTS.txt", 'r') as file:
                accounts = file.read()
                if f"Email: {em} Password: {pw}" in accounts:
                    print("Email already existing")
                    continue
                with open("D:\\DAN\\PATH\\ACCOUNTS.txt", 'a') as file:
                    account = f"Email: {em} Password: {pw}\n"
                    file.write(account)
                    print("Account Created!")
                    input("Press any key to continue....")
                    break
        else:
            print("Passwords do not match, Please try again")

def user_login():
    print('=' * 12 + ' Log in ' + '=' * 12)
    while True:
        em = input("Email: ")
        pw = input("Enter password: ")
        with open("D:\\DAN\\PATH\\ACCOUNTS.txt", 'r') as file:
            accounts = file.readlines()
            for account in accounts:
                if f"Email: {em} Password: {pw}" in account:
                    print("Log in successful")
                    login_successful = True
                    break
            if login_successful:
                lobby()
                break
            else:
                print("Wrong credentials")

def delete_account():
    print('=' * 8 + ' Delete account ' + '=' * 8)
    while True:
        em = input("Email: ")
        pw = input("Enter password: ")

        with open("D:\\DAN\\PATH\\ACCOUNTS.txt", 'r') as file: #READS ALL THE ACCOUNT
            accounts = file.readlines()

        found = False
        with open("D:\\DAN\\PATH\\ACCOUNTS.txt", 'w') as file: #IN HERE THE FILE WAS EMPTIED IN OTHER TERM THE ACCOUNTS ARE DELETED
            for account in accounts:
                if f"Email: {em} Password: {pw}" in account: # CHECKS IF THE ACCOUNT MATCHES THIS FORMAT
                    while True:
                        print("Are you sure you want to delete your account? [Y] or [N]")
                        choose = input(">> ").upper()
                        if choose == 'Y':
                            print("Account deleted successfully.")
                            found = True
                            break
                        elif choose == 'N':
                            print("Account Deletion Cancelled.")
                            file.write(account) #WRITES BACK ALL THE ACCOUNT
                            found = True
                            break
                        else:
                            print("Invalid input, please try again.")
                else:
                    file.write(account) #WRITE BACK ALL THE ACCOUNTS EXCEPT THE ACCOUNT THAT THE USER DELETED
        if not found:
            print("Wrong credentials. Please Try again")
        else:
            input("Press any key to continue....")
            break
def lobby():
    print("Welcome User!")
    input("Press any key to continue....")

looper = True
while looper:
    chooser = home()
    if chooser == 'C':
        create_acc()
    elif chooser == 'L':
        user_login()
    elif chooser == 'D':
        delete_account()
    elif chooser == 'EXIT':
        looper = False
        input("Press any key to continue....")
