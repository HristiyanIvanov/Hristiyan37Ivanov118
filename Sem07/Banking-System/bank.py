from random import randint

from accounts import Accounts
from errors import *
from users import Users


class Bank:
    def __init__(self):
        self.users = Users()
        self.accounts = Accounts(self.users)

    def register_user(self):
        print("\nOption 1: Register user selected")
        username = input("Enter a first and last name: ").title()
        try:
            first_name, last_name = username.split(" ")
        except:
            raise InvalidUserData()
        else:
            egn = input("Enter a EGN: ")
        if len(username) < 4 or not first_name.isalpha() or not last_name.isalpha():
            raise InvalidUserData()
        # egn = input("Enter a EGN: ")
        if len(egn) != 10 or not egn.isdigit():
            raise InvalidUserData()
        self.users.register_user(username, egn)
        print(f"User {username} with EGN {egn} registered successfully!")

    def create_account(self):
        print("\nOption 2: Create account selected")
        username = input("Enter your username: ")
        egn = input("Enter your EGN: ")
        currency = input("Enter the currency of the account (BGN, USD, EUR): ").upper()
        if currency == "BGN":
            iban = "BG9812"
            for i in range(0, 10):
                iban += str(randint(0, 9))
        elif currency == "USD":
            iban = "US643"
            for i in range(0, 10):
                iban += str(randint(0, 9))
        elif currency == "EUR":
            iban = "EU9414"
            for i in range(0, 10):
                iban += str(randint(0, 9))
        else:
            raise InvalidCurrencyInput()
        account_type = input("Enter the type of the account (Credit, Savings, Payment): ")
        if account_type != "Credit" and account_type != "Savings" and account_type != "Payment":
            raise InvalidAccountType()
        self.users.create_account(username, egn, iban, currency, account_type)
        print(f"Account with IBAN {iban} created successfully for user {username}!")

    def list_all_users(self):
        print("\nOption 3: List all users selected")
        self.users.list_all_users()

    def list_all_accounts(self):
        print("\nOption 4: List all accounts selected")
        username = input("Enter your username: ")
        egn = input("Enter your EGN: ")
        self.users.list_all_accounts(username, egn)

    def deposit_to_account(self):
        print("\nOption 5: Deposit to account selected")
        username = input("Enter your username: ")
        egn = input("Enter your EGN: ")
        iban = input("Enter the IBAN of the account you want to deposit to: ")
        while True:
            amount = int(input("Enter the amount you want to deposit: "))
            try:
                if amount <= 20:
                    print(f"Sorry, the amount of the deposit must be higher than 20{self.accounts.get_currency(username, egn, iban)}.")
                    continue
                break
            except ValueError:
                print("Invalid Amount Type. Please type integer number.")

        self.accounts.deposit_to_account(username, egn, iban, amount)
        print(
            f"{amount} {self.accounts.get_currency(username, egn, iban)} deposited successfully to account with IBAN {iban}!")

    def withdraw_from_account(self):
        print("\nOption 6: Withdraw from account selected")
        username = input("Enter your username: ")
        egn = input("Enter your EGN: ")
        iban = input("Enter the IBAN of the account you want to withdraw from: ")
        while True:
            amount = int(input("Enter the amount you want to deposit: "))
            try:
                if amount <= 10:
                    print(f"Sorry, you can't withdraw less then 10 {self.accounts.get_currency(username, egn, iban)}.")
                    continue
                break
            except ValueError:
                print("Invalid Amount Type. Please type integer number.")
        self.accounts.withdraw_from_account(username, egn, iban, amount)
        print(
            f"{amount} {self.accounts.get_currency(username, egn, iban)} withdrawn successfully from account with IBAN {iban}!")
