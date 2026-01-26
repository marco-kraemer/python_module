#!/usr/bin/env python3


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    plant_list = ["tomato", "lettuce", "carrots"]
    plant_list_error = ["tomato", None, "carrots"]

    print("\n\nTesting normal watering...")
    water_plants(plant_list)
    print("\n\n Testing with errors...")
    water_plants(plant_list_error)
