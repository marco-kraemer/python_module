#!/usr/bin/env python3

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
            self.__height =  height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self.__age =  age
        else:
            print(f"Invalid operation attempted: age {age} days old [REJECTED]")
            print("Security: Negative age rejected")

    def get_info(self):
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days old)"

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
    
    def get_info(self):
        return f"{self.name} (Flower): {self.get_height()}cm, {self.get_age()} days, {self.color} color"

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 1.6
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self):
        return f"{self.name} (Tree): {self.get_height()}cm, {self.get_age()} days, {self.trunk_diameter} diameter"

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def get_info(self):
        return f"{self.name} (Vegetable): {self.get_height()}cm, {self.get_age()} days, {self.harvest_season} harvest\n{self.name} is {self.nutritional_value}"


if __name__ == "__main__":
    rose = Flower("Rose", 35, 120, "Red")
    tulip = Flower("Tulip", 40, 90, "Yellow")

    oak = Tree("Oak", 500, 3650, 80)
    pine = Tree("Pine", 620, 4200, 65)

    carrot = Vegetable("Carrot", 25, 90, "Autumn", "High in Vitamin A")
    lettuce = Vegetable("Lettuce", 20, 45, "Spring", "Low calories, high fiber")

    print("=== Flowers ===")
    print(rose.get_info())
    print(tulip.get_info())

    print("\n=== Trees ===")
    print(oak.get_info())
    print(pine.get_info())

    print("\n=== Vegetables ===")
    print(carrot.get_info())
    print(lettuce.get_info())

    print("\n=== Actions ===")
    rose.bloom()
    tulip.bloom()
    oak.produce_shade()
    pine.produce_shade()

    print("\n=== Invalid value tests ===")
    rose.set_height(-10)
    pine.set_age(-500)
