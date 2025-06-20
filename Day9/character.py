# character.py

class Character:
    def __init__(self, name, health, max_health, attack_power, defense, level):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.defense = defense
        self.level = level

    def is_alive(self):
        """
        Check if character is alive.
        Returns True if health > 0, else False.
        """
        return self.health > 0

    def take_damage(self, amount):
        """
        Apply damage to character, reduced by defense.
        Health cannot go below 0.
        """
        damage_taken = amount - self.defense
        if damage_taken < 0:
            damage_taken = 0

        self.health -= damage_taken
        if self.health < 0:
            self.health = 0

        print(f"{self.name} takes {damage_taken} damage! (Health: {self.health}/{self.max_health})")

    def __str__(self):
        return (f"{self.name} | Level: {self.level}\n"
                f"Health: {self.health}/{self.max_health}\n"
                f"Attack: {self.attack_power} | Defense: {self.defense}")
