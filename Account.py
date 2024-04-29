# InjamTanvir(INJAM UL HAQUE)

import random

class Account:
    _account_numbers = set()

    def __init__(self, name, nid, email, address, account_type, password):
        self.name = name
        self.nid = nid
        self.email = email
        self.address = address
        self.account_type = account_type
        self.__balance = 0
        self.account_number = self._generate_account_number()
        self.transactions = []
        self.loans_taken = 0
        self.password = password

    def _generate_account_number(self):
        while True:
            account_number = random.randint(100000000000, 999999999999)
            if account_number not in Account._account_numbers:
                Account._account_numbers.add(account_number)
                return account_number

    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(("Deposit", amount))
        return f"Thank you!\n{amount} deposited successfully.\nYour total balance is {self.get_balance()}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Withdrawal amount exceeded"
        else:
            self.__balance -= amount
            self.transactions.append(("Withdrawal", amount))
            return f"Withdrawal of {amount} successful.\nYour total balance is {self.get_balance()}"

    def get_balance(self):
        return self.__balance

    def get_transaction_history(self):
        return self.transactions

    def take_loan(self, amount):
        if self.loans_taken >= 2:
            return "Loan limit reached"
        self.__balance += amount
        self.loans_taken += 1
        self.transactions.append(("Loan", amount))
        return f"Loan of {amount} successful.\nLoan amount added to your account.\nYour total balance is {self.get_balance()}"

    def transfer_money(self, recipient_email, amount):
        if recipient_email not in self.bank.accounts:
            return "Recipient account not found."

        recipient_account = self.bank.accounts[recipient_email]

        if self.balance < amount:
            return "Insufficient balance for transfer."

        self.balance -= amount
        recipient_account.balance += amount

        self.transactions.append(("Transfer ->", -amount))
        recipient_account.transactions.append(("Transfer <-", amount))

        return self.balance