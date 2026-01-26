#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_wilting(plant):
    raise PlantError(f"The {plant} is wilting!")


def check_water():
    raise WaterError("Not enought water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("\n\nTesting PlantError...")
    try:
        check_plant_wilting("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\n\nTesting Water Plant...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\n\nTesting catching all garden errors...")
    try:
        check_plant_wilting("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
