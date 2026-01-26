#!/usr/bin/env python3
"""
Plant Growth Simulation Module.

This module defines a Plant class that models basic plant growth
over time, including height increase and aging.
"""


class Plant:
    """
    Represents a plant with growth and aging behavior.

    Attributes:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): Initial height of the plant in centimeters.
            age (int): Initial age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, days: int) -> None:
        """
        Increase the plant's height based on the number of days.

        Args:
            days (int): Number of days of growth.
        """
        self.height += days

    def add_age(self, days: int) -> None:
        """
        Increase the plant's age.

        Args:
            days (int): Number of days to add to the plant's age.
        """
        self.age += days

    def get_info(self) -> str:
        """
        Print the plant's current information.
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    """
    Main execution block.

    Simulates one week of plant growth and displays
    height and age changes.
    """
    plant = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    h1 = plant.height
    print(plant.get_info())

    plant.add_age(6)
    plant.grow(6)

    print("=== Day 7 ===")
    h2 = plant.height
    print(plant.get_info())

    print(f"Growth this week: +{h2 - h1}cm")
