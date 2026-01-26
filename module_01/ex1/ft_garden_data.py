#!/usr/bin/env python3
"""
Garden Plant Registry Module.

This module defines a Plant class and demonstrates how to
store and display basic plant information such as name,
height, and age.
"""


class Plant:
    """
    Represents a plant in the garden registry.

    Attributes:
        name (str): Name of the plant.
        height (float): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """

    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (float): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)

    plants = [p1, p2, p3]

    print("=== Garden Plant Registry ===")

    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
