class InvalidUserData(Exception):
    def __init__(self, message="Username or EGN is invalid. Please try again.", *args: object):
        super().__init__(message, *args)


class UserNotFound(Exception):
    def __init__(self, message="User not found. Please register first.", *args: object):
        super().__init__(message, *args)


class UserAlreadyExists(Exception):
    def __init__(self, message="This username is already taken. Please choose a different username.", *args: object):
        super().__init__(message, *args)


class UserAlreadyOwnsAccount(Exception):
    pass


class AccountNotFound(Exception):
    def __init__(self, message="Account not found. Please check the IBAN and try again.", *args: object):
        super().__init__(message, *args)


class UnsufficientBalance(Exception):
    def __init__(self, message="Insufficient balance. Please enter a lower amount.", *args: object):
        super().__init__(message, *args)


class InvalidAccountData(Exception):
    def __init__(self, message="Account type is wrong or cannot be empty.", *args: object):
        super().__init__(message, *args)


class InvalidAccountType(Exception):
    def __init__(self, message="Invalid Account Type. Please try again.", *args: object):
        super().__init__(message, *args)


class InvalidAmountType(Exception):
    def __init__(self, message="Invalid Amount Type. Please type integer number.", *args: object):
        super().__init__(message, *args)


class InvalidCurrencyInput(Exception):
    def __init__(self, message="Invalid Currency Input. Please enter BGN, EUR or USD.", *args: object):
        super().__init__(message, *args)


class InvalidMenuChoice(Exception):
    def __init__(self, message="Invalid selection. Please try again.", *args: object):
        super().__init__(message, *args)
