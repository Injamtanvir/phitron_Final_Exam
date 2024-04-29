# InjamTanvir(INJAM UL HAQUE)

# USER + INTERFACE IN SAME CLASS

from Bank import Bank
from Admin import Admin


class Interface:
    def __init__(self, bank):
        self.bank = bank
        self.user = None

    def main_menu(self):
        print("#######################################################")
        print("-------------------------------------------------------")
        print("################ Welcome to Phi Bank ##################")
        print("-------------------------------------------------------")
        print("#######################################################\n")
        while True:
            print("1. User login")
            print("2. Create an Account")
            print("3. Admin Access")
            print("4. Exit")
            choice = input("Please enter your choice between(1-4): ")

            if choice == '1':
                self.user_login()
            elif choice == '2':
                self.bank.create_account()
            elif choice == '3':
                admin = Admin(self.bank)
                admin.admin_panel()
            elif choice == '4':
                print("Thank you for using our Banking system. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

    def user_login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email in self.bank.accounts and self.bank.accounts[email].password == password:
            self.user = self.bank.accounts[email]
            print("Login successful!\n")
            self.user_interface()
        else:
            print("Invalid email or password. Please try again.\n")

    def user_interface(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Take Loan")
            print("6. Transfer Money")
            print("7. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                self.transaction_history()
            elif choice == '5':
                self.take_loan()
            elif choice == '6':
                self.transfer_money()
            elif choice == '7':
                print("Logging out...")
                break
            else:
                print("Invalid option. Please try again.")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        print(self.user.deposit(amount))

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        print(self.user.withdraw(amount))

    def check_balance(self):
        print(f"Your current balance is: {self.user.get_balance()}")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.user.get_transaction_history():
            print(f"{transaction[0]}: {transaction[1]}")

    def take_loan(self):
        amount = float(input("Enter the amount to loan: "))
        print(self.user.take_loan(amount))



    def transfer_money(self):
        recipient_email = input("Enter recipient's email: ")
        if recipient_email in self.bank.accounts:
            amount = float(input("Enter the amount to transfer: "))
            if amount > 0:
                recipient = self.bank.accounts[recipient_email]
                withdrawal_result = self.user.withdraw(amount)
                deposit_result = recipient.deposit(amount)

                
                if "successful" in withdrawal_result and "successful" in deposit_result:
                    sender_balance = self.bank.accounts[self.user.email].get_balance() 
                    recipient_balance = self.bank.accounts[recipient_email].get_balance() 
                    print(withdrawal_result)
                    print(deposit_result)
                    print(f"Your total balance is {sender_balance}.") 
                    print("Thank you!")
                    print(f"{amount} deposited successfully.")
                    print(f"Recipient's total balance is {recipient_balance}.")
                else:
                    print("Transaction failed. Please try again.")
            else:
                print("Invalid amount.")
        else:
            print("Recipient's account not found.")



if __name__ == "__main__":
    bank = Bank()
    intrfc = Interface(bank)
    intrfc.main_menu()
