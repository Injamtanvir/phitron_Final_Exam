# InjamTanvir(INJAM UL HAQUE)

from Bank import Bank

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def login(self):
        while True:
            email = input("Enter admin email: ")
            password = input("Enter password: ")
            if email in self.bank.admins and self.bank.admins[email] == password:
                print("Login successful!\n")
                return True
            else:
                print("Invalid email or password. Please try again.\n")
                continue

    def add_admin(self):
        if not self.login():
            return

        new_admin_email = input("Enter new admin email: ")
        new_admin_password = input("Enter new admin password: ")
        self.bank.admins[new_admin_email] = new_admin_password
        print("New admin added successfully.")

    def view_admins(self):
        if not self.login():
            return

        print("List of Admins:")
        for email in self.bank.admins:
            print(email)

    def admin_panel(self):
        if not self.login():
            return

        while True:
            print("\nAdmin Panel")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. List All Accounts")
            print("4. Check Total Bank Balance")
            print("5. Check Total Loans Issued")
            print("6. Toggle Loan Feature")
            print("7. Add New Admin")
            print("8. View Admins")
            print("9. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.bank.create_account()

            elif choice == '2':
                account_number = int(input("Enter the account number to delete: "))
                print(self.bank.delete_account(account_number))

            elif choice == '3':
                accounts = self.bank.list_accounts()
                for acc in accounts:
                    print(f"Account Number: {acc[0]}, Name: {acc[1]}, Email: {acc[2]}, Balance: {acc[3]}")

            elif choice == '4':
                print(f"Total bank balance: {self.bank.total_balance()}")

            elif choice == '5':
                total_loans, total_loan_amount = self.bank.total_loans_issued()
                print(f"Total loans issued: {total_loans}")
                #print(f"Total loan amount issued: ${total_loan_amount}") 

            elif choice == '6':
                print(self.bank.toggle_loan_feature())

            elif choice == '7':
                self.add_admin()

            elif choice == '8':
                self.view_admins()

            elif choice == '9':
                print("Exiting admin panel.")
                break

            else:
                print("Invalid option. Please try again.")
