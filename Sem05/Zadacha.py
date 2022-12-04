class MissingParameterError(Exception):
    pass


class InvalidParameter(Exception):
    def __init__(self, invalid_parameter, *args):
        message = f"Invalid parameter: {invalid_parameter}"
        super().__init__(message, *args)


class JungleAnimal:
    def __init__(self, name, age, sound):
        if type(name) != str and type(age) != int:
            raise InvalidParameter(Exception)

        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} says {self.sound}')

    def print(self):
        pass

    def daily_task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, age, sound):
        if type(age) != int and age >= 15:
            raise InvalidParameter(Exception)

        if not sound.find('rr'):
            raise InvalidParameter(Exception)
        self.age = age
        self.sound = sound

        print.Jaguar(f'{name} {age} {sound}')
        daily_task.Jaguar()
