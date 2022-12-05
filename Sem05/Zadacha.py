import random as r


class MissingParameterError(Exception):
    def __init__(self, missing_parameter, *args):
        message = f"Missing class parameter: {missing_parameter}"
        super().__init__(message, *args)


class InvalidParameterError(Exception):
    def __init__(self, invalid_parameter, *args):
        message = f"Invalid class parameter: {invalid_parameter}"
        super().__init__(message, *args)


class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__("age")


class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        super().__init__("sound")


class JungleAnimal:
    def __init__(self, name, age, sound):
        if name is None:
            raise MissingParameterError()
        elif age is None:
            raise MissingParameterError()
        elif sound is None:
            raise MissingParameterError()

        if type(name) != str:
            raise InvalidParameterError("name")
        elif type(age) != int:
            raise InvalidAgeError()
        elif type(sound) != str:
            raise InvalidSoundError()

        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def print(self):
        pass

    def daily_task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age >= 15:
            raise InvalidAgeError()
        if self.sound.count("r") < 2:
            raise InvalidSoundError()

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for i in range(len(animals)):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                print(f"{self.name} the Jaguar hunted down {animals[i].name} the {type(animals[i]).__name__}")
                animals.pop(i)
                break


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age >= 10:
            raise InvalidAgeError()
        if self.sound.count("e") < 1:
            raise InvalidSoundError()

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self, fruits):
        if fruits >= 10:
            fruits -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits
        elif fruits > 0:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        else:
            print(f"{self.name} the Lemur couldn't find anything to eat")
            self.make_sound()
            self.make_sound()
            return 0


class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError()
        if self.sound.count("e") < 1:
            raise InvalidSoundError()

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals, buildings):
        for i in range(len(animals)):
            if animals[i] == self:
                if i != 0 and i != len(animals) - 1:
                    if type(animals[i + 1]) == Human or type(animals[i - 1]) == Human:
                        type1 = input("Enter type: ")
                        buildings.append(Building(type1))
                if i == 0:
                    if type(animals[i + 1]) == Human:
                        type1 = input("Enter type:")
                        buildings.append(Building(type1))
                if len(animals) - 1:
                    if type(animals[i - -1]) == Human:
                        type1 = input("Enter type:")
                        buildings.append(Building(type1))


class Building():
    def __init__(self, type1):
        self.type1 = type1

    def print(self):
        print(self.type1)


fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    rn = r.randint(0, 9)
    agep = r.randint(7, 20)
    name = r.randint(0, len(names) - 1)
    sound = r.randint(0, len(sounds) - 1)
    try:
        if rn >= 0 and rn <= 3:
            animals.append(Lemur(names[name], agep, sounds[sound]))
        elif rn > 3 and rn <= 7:
            animals.append(Jaguar(names[name], agep, sounds[sound]))
        elif rn > 7 and rn <= 9:
            animals.append(Human(names[name], agep, sounds[sound]))
    except InvalidAgeError:
        print(f"{names[name]} {agep} {sounds[sound]} {InvalidAgeError()}")
    except InvalidSoundError:
        print(f"{names[name]} {agep} {sounds[sound]} {InvalidSoundError()}")

print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Lemur:
        fruits = anim.daily_task(fruits)
    if type(anim) == Jaguar:
        anim.daily_task(animals)
    if type(anim) == Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
