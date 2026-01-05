#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age} days old)"

if __name__ == "__main__":
    plants_info = [
          ("Rose", 25, 30),
          ("Oak", 200, 365),
          ("Cactus", 5, 90),
          ("Sunflower", 80, 45),
          ("Fern", 15, 120)
    ]
     
    plants = []
    
    print("=== Plant Factory Output ===")

    count_plants = 0

    for name, height, age in plants_info:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.get_info()}")
        count_plants += 1
    
    print(f"\nTotal plants created: {count_plants}")
