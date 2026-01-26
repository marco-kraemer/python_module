#!/usr/bin/env python3
"""
Garden Inheritance System Module.

This module demonstrates inheritance, method overriding,
and encapsulation using different types of plants.
"""


class Plant:
    """
    Base class representing a generic plant.

    Height and age are protected to ensure only valid
    (non-negative) values are assigned.
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
        else:
            print(
                f"Invalid operation attempted:\
age {age} days old [REJECTED]"
            )
            print("Security: Negative age rejected")

    def get_info(self) -> str:
        """
        Return basic plant information.

        Returns:
            str: Plant description.
        """
        return f"{self.name} ({self.get_height()}cm,\
{self.get_age()} days old)"


class Flower(Plant):
    """
    Represents a flowering plant with a specific color.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower instance.

        Args:
            name (str): Name of the flower.
            height (int): Height in centimeters.
            age (int): Age in days.
            color (str): Flower color.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """
        Simulate the flower blooming.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """
        Return flower-specific information.

        Returns:
            str: Flower description.
        """
        return (
            f"{self.name} (Flower): {self.get_height()}cm, "
            f"{self.get_age()} days, {self.color} color"
        )


class Tree(Plant):
    """
    Represents a tree with a trunk diameter.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        """
        Initialize a Tree instance.

        Args:
            name (str): Name of the tree.
            height (int): Height in centimeters.
            age (int): Age in days.
            trunk_diameter (int): Diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculate and display the amount of shade produced by the tree.
        """
        shade: float = self.trunk_diameter * 1.6
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> str:
        """
        Return tree-specific information.

        Returns:
            str: Tree description.
        """
        return (
            f"{self.name} (Tree): {self.get_height()}cm, "
            f"{self.get_age()} days, {self.trunk_diameter} diameter"
        )


class Vegetable(Plant):
    """
    Represents a vegetable with harvest season and nutritional value.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name (str): Name of the vegetable.
            height (int): Height in centimeters.
            age (int): Age in days.
            harvest_season (str): Best harvest season.
            nutritional_value (str): Nutritional description.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
        """
        Return vegetable-specific information.

        Returns:
            str: Vegetable description.
        """
        return (
            f"{self.name} (Vegetable): {self.get_height()}cm, "
            f"{self.get_age()} days, {self.harvest_season} harvest\n"
            f"{self.name} is {self.nutritional_value}"
        )


if __name__ == "__main__":
    """
    Main execution block.

    Demonstrates inheritance, polymorphism, and validation
    across different plant types.
    """
    rose = Flower("Rose", 35, 120, "Red")
    tulip = Flower("Tulip", 40, 90, "Yellow")

    oak = Tree("Oak", 500, 3650, 80)
    pine = Tree("Pine", 620, 4200, 65)

    carrot = Vegetable("Carrot", 25, 90, "Autumn", "High in Vitamin A")
    lettuce = Vegetable("Lettuce", 20, 45, "Spring", "Low calories")

    print("=== Flowers ===")
    print(rose.get_info())
    print(tulip.get_info())

    print("\n=== Trees ===")
    print(oak.get_info())
    print(pine.get_info())

    print("\n=== Vegetables ===")
    print(carrot.get_info())
    print(lettuce.get_info())

    print("\n=== Actions ===")
    rose.bloom()
    tulip.bloom()
    oak.produce_shade()
    pine.produce_shade()

    print("\n=== Invalid value tests ===")
    rose.set_height(-10)
    pine.set_age(-500)
