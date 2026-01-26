#!/usr/bin/env python3
"""
Garden Security System Module.

This module defines a Plant class with protected attributes
and validation logic to prevent invalid state changes.
"""


class SecurePlant:
    """
    Represents a plant with secure height and age attributes.

    Height and age are protected to prevent invalid values
    such as negative numbers.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance with validation.

        Args:
            name (str): Name of the plant.
            height (int): Initial height in centimeters.
            age (int): Initial age in days.
        """
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """
        Get the plant's height.

        Returns:
            int: Height in centimeters.
        """
        return self.__height

    def get_age(self) -> int:
        """
        Get the plant's age.

        Returns:
            int: Age in days.
        """
        return self.__age

    def set_height(self, height: int) -> None:
        """
        Set the plant's height with validation.

        Args:
            height (int): New height in centimeters.
        """
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """
        Set the plant's age with validation.

        Args:
            age (int): New age in days.
        """
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(
                f"Invalid operation\
 attempted: age {age} days old [REJECTED]"
            )
            print("Security: Negative age rejected")

    def get_info(self) -> str:
        """
        Return a formatted string with plant information.

        Returns:
            str: Plant name, height, and age.
        """
        return f"{self.name} ({self.get_height()}cm,\
{self.get_age()} days old)"


if __name__ == "__main__":
    """
    Main execution block.

    Attempts to create multiple Plant objects, demonstrating
    validation and encapsulation safeguards.
    """
    plants_info = [
        ("Rose", 25, 30),
        ("Oak", 200, 0),
        ("Cactus", -5, 90),
        ("Sunflower", 80, -45),
        ("Fern", 15, 120),
    ]

    plants: list[SecurePlant] = []

    print("=== Garden Security System ===")

    for name, height, age in plants_info:
        plant = SecurePlant(name, height, age)
        plants.append(plant)
        print(f"Current plant: {plant.get_info()}\n\n")
