import random

from entities.heroequipment import *
from game.errors import *


def main():
    program = HeroFunctionsProgram()

    while True:
        print("Enter a command:")
        print("1. Create new hero")
        print("2. Equip hero")
        print("3. Equip additional item")
        print("4. View hero equipment")
        print("5. Exit")

        command = input("Command: ")

        if command == "1":
            hero_name = input("Enter hero name -> First and Last Name: ")
            gender = input("Enter Gender -> Male / Female: ")
            game_class = input("Enter Class -> Warrior, Mage, Priest or Rogue: ")
            try:
                program.create_new_hero(hero_name, gender, game_class)
                print(f"{hero_name} as {gender} -> {game_class} has been created!")
            except InvalidUserData as e:
                print(e)
            except InvalidDataError as e:
                print(e)
            except CharacterExists as e:
                print(e)
            except InvalidGender as e:
                print(e)
            except InvalidClass as e:
                print(e)

        elif command == "2":
            hero_name = input("Enter hero name: ")
            item_name = input("Enter item name: ")
            attack_dmg = random.randint(20, 500)
            attack_dmg = f"{attack_dmg} AD"
            try:
                program.equip_hero(hero_name, item_name, attack_dmg)
                print(f"{item_name} with: {attack_dmg} has been equipped to {hero_name}!")
            except InvalidDataError as e:
                print(e)
            except InvalidUserData as e:
                print(e)

        elif command == "3":
            hero_name = input("Enter hero name: ")
            item_name = input("Enter item name: ")
            item_type = input("Enter item type: ")
            durability = random.randint(100, 800)
            durability = f"{durability} DUR"
            try:
                program.equip_additional_item(hero_name, item_name, item_type, durability)
                print(
                    f"Addition item: {item_name} from type: {item_type} and {durability} has been equipped to {hero_name}!")
            except InvalidDataError as e:
                print(e)
            except InvalidUserData as e:
                print(e)

        elif command == "4":
            hero_name = input("Enter hero name: ")
            try:
                program.view_hero_equipment(hero_name)
            except InvalidDataError as e:
                print(e)
            except InvalidUserData as e:
                print(e)

        elif command == "5":
            print("Exiting program...")
            break

        else:
            raise InvalidCommandError()


if __name__ == "__main__":
    main()
