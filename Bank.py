# InjamTanvir(INJAM UL HAQUE)

from Account import Account


class Bank:
    def __init__(self):
        self.accounts = {}
        self.admins = {"naimvai@gmail.com": "naim123", "injam@gmail.com": "Injam123"}  # Store admin accounts
        self.loan_feature_enabled = True

    def store_account(self, name, nid, email, address, account_type, password):
        new_account = Account(name, nid, email, address, account_type, password)
        self.accounts[new_account.account_number] = new_account
        return new_account.account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            deleted_account_name = self.accounts[account_number].name
            del self.accounts[account_number]
            return f"Account {account_number} with name {deleted_account_name} deleted successfully."
        else:
            return "Account not found."

    def list_accounts(self):
        return [(acc_num, acc.name, acc.email, acc.get_balance()) for acc_num, acc in self.accounts.items()]

    def total_balance(self):
        return sum(account.get_balance() for account in self.accounts.values())

    def total_loans_issued(self):
            total_loans = 0
            total_loan_amount = 0

            for account in self.accounts.values():
                total_loans += account.loans_taken
                total_loan_amount += sum(transaction[1] for transaction in account.transactions if transaction[0] == "Loan -> ")

            return total_loans, total_loan_amount

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        return "Loan feature enabled" if self.loan_feature_enabled else "Loan feature disabled"

    def create_account(self):
        name = input("Enter your name: ")
        NID = input("Enter NID number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (Savings/Current): ")
        password = input("Please Enter a Strong Password: ")

        if email in self.accounts:
            print("This email is already in use.")
            return
        else:
            new_account = Account(name, NID, email, address, account_type, password)
            self.accounts[email] = new_account
            print(f"Account created successfully.\nWelcome to Phi Bank!! {name}\nYour account number is {new_account.account_number}")
