#!/usr/bin/env python3


class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_plants(self):
        print(f"{self.name} is helping all plants grow")
        for plant in self.plants:
            plant.grow()


class GardenManager:
    gardens = 0

    def __init__(self):
        self.gardens = {}

    def add_garden(self, garden):
        GardenManager.gardens += 1
        self.gardens[garden.name] = garden

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def count_plants(self):
            count = 0
            for _ in self.garden.plants:
                count += 1
            return count

        def plant_types(self):
            regular = flowering = prize_flower = 0
            for plant in self.garden.plants:
                if plant.get_type() == "regular":
                    regular += 1
                elif plant.get_type() == "flowering":
                    flowering += 1
                elif plant.get_type() == "prize flower":
                    prize_flower += 1
            return regular, flowering, prize_flower

    def report(self, name):
        garden = self.gardens[name]
        stats = GardenManager.GardenStats(garden)
        print(f"=== {garden.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"- {plant.get_info()}")

        regular, flowering, prize_flower = stats.plant_types()
        print(
            f"\nPlants added: {stats.count_plants()},\
Total growth: {stats.count_plants()}"
        )
        print(
            f"Plant types: {regular} regular, {flowering} flowering,\
{prize_flower} prize_flower"
        )

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.gardens}")

    @staticmethod
    def height_validation(height):
        if height >= 0:
            return True
        else:
            return False


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, height):
        if height >= 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print(
                f"Invalid operation attempted:\
age {age} days old [REJECTED]"
            )
            print("Security: Negative age rejected")

    def get_info(self):
        return f"{self.name} (Regular): {self.get_height()}cm,\
{self.get_age()} days old"

    def grow(self):
        self.set_height(self.get_height() + 1)
        print(f"{self.name} grew 1cm ({self.get_height()}cm now).")

    def get_type(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        return f"{self.name} (Flowering): {self.get_height()}cm,\
{self.get_age()} days, {self.color} flowers (blooming)"

    def get_type(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize):
        super().__init__(name, height, age, color)
        self.prize = prize

    def get_info(self):
        return f"{self.name} (Prize Flower): {self.get_height()}cm,\
{self.get_age()} days, {self.color} flowers (blooming),\
{self.prize} prize flowers"

    def get_type(self):
        return "prize flower"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n\n")
    garden_manager = GardenManager()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")
    charlie_garden = Garden("Charlie")

    garden_manager.add_garden(alice_garden)
    garden_manager.add_garden(bob_garden)
    garden_manager.add_garden(charlie_garden)

    oak = Plant("Oak Tree", 100, 30)
    rose = FloweringPlant("Rose", 25, 90, "red")
    sunflower = PrizeFlower("Sunflower", 50, 12, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    print("\n")
    bob_garden.add_plant(oak)
    bob_garden.add_plant(sunflower)
    print("\n")
    charlie_garden.add_plant(rose)
    print("\n")
    alice_garden.grow_plants()
    print("\n")
    alice_garden.grow_plants()
    print("\n")
    alice_garden.grow_plants()
    print("\n")
    bob_garden.grow_plants()
    print("\n")
    charlie_garden.grow_plants()
    print("\n")
    print(
        f"Height validation test:\
{GardenManager.height_validation(rose.get_height())}"
    )
    print("\n")
    garden_manager.report("Alice")
    print("\n")
    garden_manager.report("Bob")
    GardenManager.create_garden_network()
