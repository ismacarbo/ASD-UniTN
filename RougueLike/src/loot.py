import random

class Loot:
    def __init__(self, name,weigth,value,typeLoot):
        self.name=name
        self.weight=weigth
        self.value=value
        self.typeLoot=typeLoot

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Weight: {self.weight}, Value: {self.value})"

LOOT_POOL = [
    Loot("Sword", 5, 10, "weapon"),
    Loot("Health Potion", 2, 20, "potion"),
    Loot("Key", 1, 0, "key"),
    Loot("Gold Coin", 1, 5, "currency"),
    Loot("Shield", 4, 8, "armor"),
    Loot("Food", 3, 6, "food")
]

def random_loot():
    return random.choice(LOOT_POOL)