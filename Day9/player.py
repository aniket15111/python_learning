# player.py

from character import Character

class Player(Character):
    def __init__(self, name):
        # Call the Character init to set shared attributes
        super().__init__(
            name=name,
            health=100,
            max_health=100,
            attack_power=10,
            defense=5,
            level=1
        )
        
        # Player-specific attributes
        self.xp = 0
        self.gold = 0
        self.inventory = []
        self.special_ability_ready = False

    def gain_experience(self, xp_amount):
        self.xp += xp_amount
        xp_needed = self.level ** 2 * 100
        if xp_needed <= self.xp:
            self.level_up()

    def level_up(self):
        old_attack = self.attack_power
        old_defense = self.defense
        old_max_health = self.max_health

        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack_power += 5
        self.defense += 2

        xp_needed = (self.level - 1) ** 2 * 100
        self.xp -= xp_needed

        print(f"\n🎉 {self.name} leveled up to Level {self.level}!")
        print(f"❤️ Max Health: {old_max_health} → {self.max_health}")
        print(f"🗡️ Attack Power: {old_attack} → {self.attack_power}")
        print(f"🛡️ Defense: {old_defense} → {self.defense}\n")

    def use_item(self, item):
        if item in self.inventory:
            if item == 'Healing Potion':
                heal_amount = 50 + self.level * 5
                self.health += heal_amount
                if self.health > self.max_health:
                    self.health = self.max_health

                print(f"{self.name} used {item} and healed {heal_amount} health. New health is {self.health}")

                self.inventory.remove(item)
            else:
                print(f"{item} has no effect (yet).")
        else:
            print(f"{item} not found in inventory.")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"👜 New item added to inventory: {item}")

    def attack(self, target):
        if target.is_alive():
            target.take_damage(self.attack_power)
            print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        else:
            print(f"{target.name} is already defeated!")

    def __str__(self):
        return (f"Player: {self.name}\n"
                f"Level: {self.level} (XP: {self.xp})\n"
                f"Health: {self.health}/{self.max_health}\n"
                f"Attack: {self.attack_power} | Defense: {self.defense}\n"
                f"Gold: {self.gold}\n"
                f"Inventory: {self.inventory}\n")
