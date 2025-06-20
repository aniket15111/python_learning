from character import Character
from player import Player

class Enemy(Character):
    def __init__(self, name):
        super().__init__(
            name=name, 
            health=0, 
            max_health=0, 
            attack_power=0, 
            defense=0, 
            level=1
        )

        self.enemy_type = name.lower()
        self.loot_gold = 0
        self.loot_item = None

        if self.enemy_type == 'goblin':
            self.health = 30
            self.max_health = 30
            self.attack_power = 5
            self.defense = 1
            self.level = 1
            self.loot_gold = 10
            self.loot_item = "Healing Potion"

        elif self.enemy_type == 'orc':
            self.health = 50
            self.max_health = 50
            self.attack_power = 8
            self.defense = 3
            self.level = 2
            self.loot_gold = 20
            self.loot_item = "Sword Fragment"

        elif self.enemy_type == 'dragon':
            self.health = 150
            self.max_health = 150
            self.attack_power = 20
            self.defense = 8
            self.level = 5
            self.loot_gold = 100
            self.loot_item = "Legendary Treasure"

        else:
            print(f"⚠️ Unknown enemy type: {name}. Setting as weak goblin.")
            self.health = 10
            self.max_health = 10
            self.attack_power = 3
            self.defense = 0
            self.level = 1
            self.loot_gold = 5
            self.loot_item = None

    def attack(self, target):
        if target.is_alive():
            target.take_damage(self.attack_power)
            print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        else:
            print(f"{target.name} is already defeated.")
    def loot_dropped(self):
        return (self.loot_gold, self.loot_item)


            
          