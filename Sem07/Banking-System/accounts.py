from users import *


class Accounts:
    def __init__(self, users):
        self.users = users

    def get_user(self, username, egn):
        user = self.users.find_user(username, egn)
        # for user in self.users:
        if user["username"] == username:
            if egn and user["egn"] == egn:
                return user
            elif not egn:
                return user
        return None

    def get_account(self, user, iban):
        for account in user["accounts"]:
            if account["iban"] == iban:
                return account
        return None

    def get_currency(self, username, egn, iban):
        user = self.get_user(username, egn)
        if not user:
            raise UserNotFound()
        account = self.get_account(user, iban)
        if not account:
            raise AccountNotFound()
        return account["currency"]

    def deposit_to_account(self, username, egn, iban, amount):
        user = self.get_user(username, egn)
        if not user:
            raise UserNotFound()
        account = self.get_account(user, iban)
        if not account:
            raise AccountNotFound()
        if type(amount) != int:
            raise InvalidAmountType()
        account["balance"] += amount

    def withdraw_from_account(self, username, egn, iban, amount):
        user = self.get_user(username, egn)
        if not user:
            raise UserNotFound()
        account = self.get_account(user, iban)
        if not account:
            raise AccountNotFound()
        if amount > account["balance"]:
            raise UnsufficientBalance()
        if type(amount) != int:
            raise InvalidAmountType()
        account["balance"] -= amount
