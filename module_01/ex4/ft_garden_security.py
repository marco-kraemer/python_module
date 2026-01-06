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
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self.__age =  age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age}days old [REJECTED]")
            print("Security: Negative age rejected")

    def get_info(self):
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days old)"


if __name__ == "__main__":
    plants_info = [
        ("Rose", 25, 30),
        ("Oak", 200, 0),
        ("Cactus", -5, 90),
        ("Sunflower", 80, -45),
        ("Fern", 15, 120)
    ]

    plants = []
    
    print("=== Garden Security System ===")

    for name, height, age in plants_info:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Current plant: {plant.get_info()}")
