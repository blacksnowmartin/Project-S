import random

class SissyCrossdresserGame:
    def __init__(self):
        self.items = [
            "Lace Dress",
            "High Heels",
            "Makeup Kit",
            "Wig",
            "Stockings",
            "Jewelry",
            "Purse"
        ]
        self.player_items = []

    def buy_item(self):
        item = random.choice(self.items)
        self.player_items.append(item)
        return item

    def show_items(self):
        return self.player_items

game = SissyCrossdresserGame()

# Simulate buying items
for _ in range(3):
    print(f"You bought: {game.buy_item()}")

print(f"Your items: {game.show_items()}")
