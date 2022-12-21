from game import errors


class Hero:
    def __init__(self, name, egn, gender, game_class):
        self.name = name
        self.egn = egn
        self.gender = gender
        self.game_class = game_class
        self.equipped_items = []

    def equip_item(self, item_name, attack_dmg):
        self.equipped_items.append(item_name, attack_dmg)

    def equip_additional_item(self, item_name, item_type):
        self.equipped_items.append((item_name, item_type))

    def view_equipment(self):
        print(f"{self.name}'s equipment:")
        for item in self.equipped_items:
            print(f" - {item}")


class HeroEquipmentProgram:
    def __init__(self):
        self.heroes = {}

    def create_new_hero(self, hero_name, egn, gender, game_class):
        try:
            first_name, last_name = hero_name.split(" ")
        except:
            raise errors.InvalidUserData()
        else:
            if len(hero_name) < 4:
                raise errors.InvalidUserData()
            if len(egn) != 10 or not egn.isdigit():
                raise errors.InvalidUserData()
            if gender != "Male" and gender != "Female":
                raise errors.InvalidGender()
            if game_class != "Warrior" and game_class != "Mage" and game_class != "Priest" and game_class != "Rogue":
                raise errors.InvalidClass()
        if hero_name in self.heroes:
            raise errors.CharacterExists()

        self.heroes[hero_name, egn, gender, game_class] = Hero(hero_name, egn, gender, game_class)

    def equip_hero(self, hero_name, item_name, attack_dmg):
        if hero_name not in self.heroes:
            raise errors.InvalidDataError()

        self.heroes[hero_name].equip_item(item_name, attack_dmg)

    def equip_additional_item(self, hero_name, item_name, item_type):
        if hero_name not in self.heroes:
            raise errors.InvalidDataError()

        self.heroes[hero_name].equip_additional_item(item_name, item_type)

    def view_hero_equipment(self, hero_name):
        if hero_name not in self.heroes:
            raise errors.InvalidDataError()

        self.heroes[hero_name].view_equipment()
