#!/usr/bin/env python3

# =========================
# Plant family hierarchy
# =========================

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_type(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def get_type(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_type(self):
        return "prize"


# =========================
# Garden
# =========================

class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()


# =========================
# Garden Manager
# =========================

class GardenManager:
    total_gardens = 0

    def __init__(self):
        self.gardens = {}
        GardenManager.total_gardens += 1

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def plant_count(self):
            return len(self.garden.plants)

        def total_growth(self):
            return len(self.garden.plants)

        def plant_types(self):
            regular = flowering = prize = 0
            for plant in self.garden.plants:
                if plant.get_type() == "regular":
                    regular += 1
                elif plant.get_type() == "flowering":
                    flowering += 1
                elif plant.get_type() == "prize":
                    prize += 1
            return regular, flowering, prize

        def garden_score(self):
            score = 0
            for plant in self.garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            return score

    def add_garden(self, garden):
        self.gardens[garden.owner] = garden

    def report(self, owner):
        garden = self.gardens[owner]
        stats = GardenManager.GardenStats(garden)

        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming), Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")

        r, f, p = stats.plant_types()
        print(f"Plants added: {stats.plant_count()}, Total growth: {stats.total_growth()}cm")
        print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers")

    @classmethod
    def create_garden_network(cls):
        return f"Total gardens managed: {cls.total_gardens}"

    @staticmethod
    def validate_height(height):
        return height >= 0


# =========================
# Demo / main
# =========================

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.help_plants_grow()

    manager.report("Alice")

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    print(f"Garden scores - Alice: {GardenManager.GardenStats(alice_garden).garden_score()}, "
          f"Bob: {GardenManager.GardenStats(bob_garden).garden_score()}")

    print(GardenManager.create_garden_network())
