from errors import *


class Users:
    def __init__(self):
        self.users = []

    def register_user(self, username, egn):
        if not username or not egn:
            raise InvalidUserData()
        if self.get_user(username):
            raise UserAlreadyExists()
        user = {
            "username": username,
            "egn": egn,
            "accounts": []
        }
        # self.users.append({"username": username, "egn": egn, "accounts": []})
        self.users.append(user)

    def create_account(self, username, egn, iban, currency, account_type):
        user = self.get_user(username, egn)
        if not user:
            raise UserNotFound()
        if self.get_account(user, iban):
            raise UserAlreadyOwnsAccount(
                f"User {username} already owns an account with this IBAN. Please choose a different IBAN.")
        if not currency or not account_type:
            raise InvalidAccountData()
        account = {
            "iban": iban,
            "currency": currency,
            "account_type": account_type,
            "balance": 0
        }
        user["accounts"].append(account)

    def list_all_users(self):
        if not self.users:
            print("No users found.")
        else:
            print("Users:")
            for user in self.users:
                print(f"Username: {user['username']}, EGN: {user['egn']}")

    def list_all_accounts(self, username, egn):
        user = self.get_user(username, egn)
        if not user:
            raise UserNotFound()
        if not user["accounts"]:
            print("No accounts found for this user.")
        else:
            print("Accounts:")
            for account in user["accounts"]:
                print(
                    f"IBAN: {account['iban']}, Currency: {account['currency']}, Account type: {account['account_type']}, Balance: {account['balance']}")

    def get_user(self, username, egn=None):
        for user in self.users:
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

    def find_user(self, username, egn):
        for user in self.users:
            if user["username"] == username:
                if egn and user["egn"] == egn:
                    return user
                elif not egn:
                    return user
        return None
