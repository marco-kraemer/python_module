#!/usr/bin/env python3
"""
Custom Garden Exceptions Demo.

This module demonstrates how to define and use custom exceptions
with inheritance to represent domain-specific errors in a garden
management system.
"""


class GardenError(Exception):
    """
    Base exception class for all garden-related errors.
    """

    pass


class PlantError(GardenError):
    """
    Exception raised for plant-related issues.
    """

    pass


class WaterError(GardenError):
    """
    Exception raised for water-related issues in the garden.
    """

    pass


def check_plant_wilting(plant: str) -> None:
    """
    Check if a plant is wilting and raise an error if it is.

    Args:
        plant (str): Name of the plant being checked.

    Raises:
        PlantError: If the plant is wilting.
    """
    raise PlantError(f"The {plant} is wilting!")


def check_water() -> None:
    """
    Check water availability and raise an error if insufficient.

    Raises:
        WaterError: If there is not enough water in the tank.
    """
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    """
    Main execution block.

    Demonstrates catching specific garden-related errors
    as well as catching all garden errors via the base exception.
    """
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant_wilting("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant_wilting("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
