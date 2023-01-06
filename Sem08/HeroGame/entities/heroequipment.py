from game.entities.heros import *
from game.errors import *


class HeroFunctionsProgram:
    def __init__(self):
        self.heroes = {}

    def create_new_hero(self, hero_name, gender, game_class):
        try:
            first_name, last_name = hero_name.split(" ")
        except:
            raise InvalidUserData()
        if len(hero_name) < 4:
            raise InvalidUserData()
        if gender != "Male" and gender != "Female":
            raise InvalidGender()
        if game_class != "Warrior" and game_class != "Mage" and game_class != "Priest" and game_class != "Rogue":
            raise InvalidClass()
        if hero_name in self.heroes:
            raise CharacterExists()

        self.heroes[hero_name] = Hero(hero_name, gender, game_class)

    def equip_hero(self, hero_name, item_name, attack_dmg):
        if hero_name not in self.heroes:
            raise InvalidDataError()

        self.heroes[hero_name].equip_item(item_name, attack_dmg)

    def equip_additional_item(self, hero_name, item_name, item_type, durability):
        if hero_name not in self.heroes:
            raise InvalidDataError()

        self.heroes[hero_name].equip_additional_item(item_name, item_type, durability)

    def view_hero_equipment(self, hero_name):
        if hero_name not in self.heroes:
            raise InvalidDataError()

        self.heroes[hero_name].view_equipment()
