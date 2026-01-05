#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def grow(self, days):
        self.height += days
    
    def add_age(self, days):
        self.age += days
    
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    h1 = plant.height
    plant.get_info()
    plant.add_age(6)
    plant.grow(6)
    print("=== Day 7 ===")
    h2 = plant.height
    plant.get_info()
    print(f"Growth this week: +{h2 - h1}cm")