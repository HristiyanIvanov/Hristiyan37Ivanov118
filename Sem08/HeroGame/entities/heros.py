class Hero:
    def __init__(self, name, gender, game_class):
        self.name = name
        self.gender = gender
        self.game_class = game_class
        self.equipped_items = []

    def equip_item(self, item_name, attack_dmg):
        self.equipped_items.append((item_name, attack_dmg))

    def equip_additional_item(self, item_name, item_type, durability):
        self.equipped_items.append((item_name, item_type, durability))

    def view_equipment(self):
        print(f"{self.name}'s equipment:")
        for item in self.equipped_items:
            print(f" - {item}")
