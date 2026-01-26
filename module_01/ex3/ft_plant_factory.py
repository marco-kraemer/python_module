#!/usr/bin/env python3
"""
Plant Factory Module.

This module creates Plant objects from predefined data
and displays information about each created plant.
"""


class Plant:
    """
    Represents a plant with basic descriptive information.

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
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """
        Return a formatted string with the plant's information.

        Returns:
            str: Plant description including name, height, and age.
        """
        return f"{self.name} ({self.height}cm, {self.age} days old)"


if __name__ == "__main__":
    """
    Main execution block.

    Creates multiple Plant objects using predefined data
    and prints their information along with a total count.
    """
    plants_info = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants: list[Plant] = []

    print("=== Plant Factory Output ===")

    count_plants: int = 0

    for name, height, age in plants_info:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.get_info()}")
        count_plants += 1

    print(f"\nTotal plants created: {count_plants}")
