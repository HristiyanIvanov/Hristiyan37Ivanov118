class InvalidUserData(Exception):
    def __init__(self, message="Hero Name or EGN is invalid. Please try again.", *args: object):
        super().__init__(message, *args)


class CharacterExists(Exception):
    def __init__(self, message="Hero with this name already exists!", *args: object):
        super().__init__(message, *args)


class InvalidDataError(Exception):
    def __init__(self, message="Hero with this name does not exists!", *args: object):
        super().__init__(message, *args)


class InvalidCommandError(Exception):
    def __init__(self, message="Invalid command entered!", *args: object):
        super().__init__(message, *args)

class InvalidGender(Exception):
    def __init__(self, message="The Gender of the Hero can be only Male or Female.", *args: object):
        super().__init__(message, *args)


class InvalidClass(Exception):
    def __init__(self, message="Hero's class can be from 1-5.", *args: object):
        super().__init__(message, *args)
