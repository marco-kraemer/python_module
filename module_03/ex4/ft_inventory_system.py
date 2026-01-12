#!/usr/bin/env python3

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
    
    def add_item(self, item_name, quantity):
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
    
    def update_item_quantity(self, item_name, quantity):
        self.inventory.update({item_name: quantity})
    
class Inventory:
    def __init__(self, items):
        self.items = items

    def get_player_inventory(self, player_inventory):
        s = ""
        for item in player_inventory:
            category = self.items[item]["category"]
            rarity = self.items[item]["rarity"]
            quantity = player_inventory[item]
            price = self.items[item]["price"]
            s += f"{item} ({category}, {rarity}): {quantity}x @ {price} gold each = {price * quantity} gold\n"
        return s

    def get_player_inventory_value(self, player_inventory):
        total_value = 0
        total_items = 0
        for item in player_inventory:
            total_value += self.items[item]["price"] * player_inventory[item]
            total_items += player_inventory[item]
        return f"\nInventory value: {total_value} gold\nItem count: {total_items} items"

    def get_player_inventory_categories(self, player_inventory):
        categories = {}
        for item in player_inventory:
            category = self.items[item]["category"]
            quantity = player_inventory[item]
            categories[category] = categories.get(category, 0) + quantity
        return f"Categories: {categories}"

print("=== Player Inventory System ===")

items = {"sword": {"category": "weapon", "rarity": "rare", "price": 500},
         "potion": {"category": "consumable", "rarity": "common", "price": 50},
         "shield": {"category": "armor", "rarity": "uncommon", "price": 200},
         "magic_ring": {"category": "weapon", "rarity": "rare", "price": 2500}}

inventory = Inventory(items)

alice = Player("alice")
alice.add_item("sword", 1)
alice.add_item("potion", 5)
alice.add_item("shield", 1)

print("\n=== Alice's Inventory ===")
print(inventory.get_player_inventory(alice.inventory))
print(inventory.get_player_inventory_value(alice.inventory))
print(inventory.get_player_inventory_categories(alice.inventory))


print("\n=== Transaction: Alice gives Bob 2 portions ===")
bob = Player("bob")
alice.update_item_quantity("potion", 3)
bob.update_item_quantity("potion", 2)
print("Transaction successful!")
print("\n=== Updated Inventories ===")
print(f"Alice potions: {alice.inventory['potion']}")
print(f"Bob potions: {bob.inventory['potion']}")

print("\n=== Inventory Analytics ===")

players = {
    "Alice": alice,
    "Bob": bob
}

most_value = 0
most_value_player = None

for player in players.values():
    value = 0
    for item, qty in player.inventory.items():
        value += inventory.items[item]["price"] * qty
    if value > most_value:
        most_value = value
        most_value_player = player.name

print(f"Most valuable player: {most_value_player} ({most_value} gold)")

most_items = 0
most_items_player = None

for player in players.values():
    count = sum(player.inventory.values())
    if count > most_items:
        most_items = count
        most_items_player = player.name

print(f"Most items: {most_items_player} ({most_items} items)")

rarity_rank = {
    "common": 1,
    "uncommon": 2,
    "rare": 3,
}

highest_rarity = 0

for data in items.values():
    rank = rarity_rank[data["rarity"]]
    if rank > highest_rarity:
        highest_rarity = rank

rarest_items = []

for item, data in items.items():
    if rarity_rank[data["rarity"]] == highest_rarity:
        rarest_items.append(item)

print("Rarest items: " + ", ".join(rarest_items))
