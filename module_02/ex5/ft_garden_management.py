#!/usr/bin/env python3

class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class Plant:
    def __init__(self, plant, water_level, sunlight_hours):
        if not plant or not water_level or not sunlight_hours:
            raise ("Plant Creation - Values cannot be empty!")
        self.plant = plant
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plants(self, plant):
        if not plant:
            raise PlantError("adding plant (Plant name cannot be empty!)")
        self.plants.append(plant)
        print(f"Added {plant.plant} successfully!")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant.water_level += 1
                print(f"Watering {plant.plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant):
        if not plant.plant:
            raise PlantError("Plant name cannot be empty!")
        elif plant.water_level > 10:
            raise PlantError(f"checking {plant.plant}: Water level {plant.water_level} is too high (max 10)")
        elif plant.water_level < 1:
            raise PlantError(f"checking {plant.plant}: Water level {plant.water_level} is too low (min 1)")
        elif plant.sunlight_hours > 12:
            raise PlantError(f"checking {plant.plant}: Sunlight hours {plant.sunlight_hours} is too high (max 12)")
        elif plant.sunlight_hours < 2:
            raise PlantError(f"checking {plant.plant}: Sunlight hours {plant.sunlight_hours} is too low (min 2)")
        return f"{plant.plant}: healthy (water: {plant.water_level}, sun: {plant.sunlight_hours})"

def garden_manager():
    print("=== Garden Management System ===")
    garden = GardenManager()
 
    print("\n\nAdding plants to garden...")
    try:
        tomato = Plant("tomato", 3, 5)
        lettuce = Plant("lettuce", 7, 2)
        carrot = Plant("carrot", 25, 80)
    except PlantError as e:
        print(f"Error: {e}")


    try:
        garden.add_plants(tomato)
        garden.add_plants(lettuce)
        garden.add_plants(carrot)
    except PlantError as e:
        print(f"Error: {e}")

    try:
        garden.add_plants(None)
    except PlantError as e:
        print(f"Error: {e}")
    
    print ("\n\nWatering plants...")
    garden.water_plants()

    print("\n\nChecking plant health...")
    try:
        print(garden.check_plant_health(tomato))
        print(garden.check_plant_health(lettuce))
        print(garden.check_plant_health(carrot))
    except PlantError as e:
        print(f"Error {e}")

    print ("\n\nWatering plants...")
    garden.water_plants()
    garden.water_plants()
    garden.water_plants()

    print("\n\nChecking plant health...")
    try:
        print(garden.check_plant_health(tomato))
        print(garden.check_plant_health(lettuce))
        print(garden.check_plant_health(carrot))
    except PlantError as e:
        print(f"Error {e}")

if __name__ == "__main__":
    garden_manager()