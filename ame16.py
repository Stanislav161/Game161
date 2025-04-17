from abc import ABC, abstractmethod


# Шаг 1: Создание абстрактного класса Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def __init__(self):
        self.name = "меч"

    def attack(self):
        return ("Боец наносит удар мечом", 10)


class Bow(Weapon):
    def __init__(self):
        self.name = "лук"

    def attack(self):
        return ("Боец наносит удар из лука", 8)


# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"Боец выбирает {weapon.name}.")

    def perform_attack(self, monster):
        if not self.weapon:
            print("Боец без оружия!")
            return

        attack_message, damage = self.weapon.attack()
        print(attack_message)
        monster.take_damage(damage)

        if monster.is_defeated():
            print("Монстр побежден!")


# Класс Monster
class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

    def is_defeated(self):
        return self.health <= 0


# Шаг 4: Реализация боевого механизма
if __name__ == "__main__":
    # Создание персонажей
    fighter = Fighter()
    monsters = [Monster(10), Monster(8)]  # Монстры с разным здоровьем

    # Бой с разным оружием
    weapons = [Sword(), Bow()]

    for weapon, monster in zip(weapons, monsters):
        fighter.change_weapon(weapon)
        fighter.perform_attack(monster)
        print()
