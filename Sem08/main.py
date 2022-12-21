import errors
from entities.hero import HeroEquipmentProgram
import random

def main():
    program = HeroEquipmentProgram()

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
            egn = input("Enter a EGN: ")
            gender = input("Enter Gender -> Male / Female: ")
            game_class = input("Enter Class -> Warrior, Mage, Priest or Rogue: ")
            try:
                program.create_new_hero(hero_name, egn, gender, game_class)
                print(f"{hero_name} with {egn} and {gender} from {game_class} has been created!")
            except errors.InvalidDataError as e:
                print(e)
            except errors.CharacterExists as e:
                print(e)
            except errors.InvalidGender as e:
                print(e)
            except errors.InvalidClass as e:
                print(e)

        elif command == "2":
            hero_name = input("Enter hero name: ")
            item_name = input("Enter item name: ")
            attack_dmg = random.randint(100,800)
            try:
                program.equip_hero(hero_name, item_name, attack_dmg)
                print(f"{item_name} with AD: {attack_dmg} has been equipped to {hero_name}!")
            except errors.InvalidDataError as e:
                print(e)
            except errors.InvalidUserData as e:
                print(e)

        elif command == "3":
            hero_name = input("Enter hero name: ")
            item_name = input("Enter item name: ")
            item_type = input("Enter item type: ")
            try:
                program.equip_additional_item(hero_name, item_name, item_type)
                print(f"Addition item: {item_name} from type: {item_type} has been equipped to {hero_name}!")
            except errors.InvalidDataError as e:
                print(e)
            except errors.InvalidUserData as e:
                print(e)

        elif command == "4":
            hero_name = input("Enter hero name: ")
            try:
                program.view_hero_equipment(hero_name)
            except errors.InvalidDataError as e:
                print(e)
            except errors.InvalidUserData as e:
                print(e)

        elif command == "5":
            print("Exiting program...")
            break

        else:
            raise errors.InvalidCommandError()


if __name__ == "__main__":
    main()
