#!/usr/bin/env python3
"""
Garden Guardian – Error Handling Demonstration.

This module demonstrates:
- Custom exception hierarchies
- Domain-specific error handling
- Input validation
- try / except / finally usage
- Error recovery (system keeps running)
"""


class GardenError(Exception):
    """Base class for all garden-related exceptions."""

    pass


class PlantError(GardenError):
    """Exception raised for plant-related errors."""

    pass


class Plant:
    """
    Represents a plant with water and sunlight requirements.
    """

    def __init__(
        self,
        plant: str,
        water_level: int,
        sunlight_hours: int,
    ) -> None:
        """
        Initialize a Plant with validation.

        Raises:
            PlantError: If provided values are invalid.
        """
        if not plant:
            raise PlantError(
                "Plant creation failed:\
 name cannot be empty"
            )
        if water_level < 0:
            raise PlantError(
                "Plant creation failed:\
 water level cannot be negative"
            )
        if sunlight_hours < 0:
            raise PlantError(
                "Plant creation failed:\
 sunlight hours cannot be negative"
            )

        self.plant: str = plant
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours


class GardenManager:
    """
    Manages garden operations such as adding plants, watering,
    and checking plant health.
    """

    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden.

        Raises:
            PlantError: If plant is invalid.
        """
        if not isinstance(plant, Plant):
            raise PlantError("Add plant failed: invalid plant object")

        self.plants.append(plant)
        print(f"Added {plant.plant} successfully!")

    def water_plants(self) -> None:
        """
        Water all plants with guaranteed cleanup.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant.water_level += 1
                print(f"Watering {plant.plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant: Plant) -> str:
        """
        Check plant health based on water and sunlight levels.

        Raises:
            PlantError: If plant health conditions are violated.
        """
        if not isinstance(plant, Plant):
            raise PlantError("Health check failed: invalid plant")

        if plant.water_level > 10:
            raise PlantError(
                f"{plant.plant}: water level \
{plant.water_level} too high (max 10)"
            )
        if plant.water_level < 1:
            raise PlantError(
                f"{plant.plant}: water level \
{plant.water_level} too low (min 1)"
            )
        if plant.sunlight_hours > 12:
            raise PlantError(
                f"{plant.plant}: sunlight {plant.sunlight_hours}\
 too high (max 12)"
            )
        if plant.sunlight_hours < 2:
            raise PlantError(
                f"{plant.plant}: sunlight \
{plant.sunlight_hours} too low (min 2)"
            )

        return (
            f"{plant.plant}: healthy "
            f"(water={plant.water_level}, sun={plant.sunlight_hours})"
        )


def test_garden_management() -> None:
    """
    Demonstrates full garden management workflow with error handling.
    """
    print("=== Garden Management System ===")
    garden = GardenManager()

    print("\nAdding plants to garden...")
    try:
        tomato = Plant("tomato", 3, 5)
        lettuce = Plant("lettuce", 7, 2)
        carrot = Plant("carrot", 25, 80)
        _ = Plant("", -1, -5)  # invalid
    except PlantError as e:
        print(f"Creation error: {e}")
    finally:
        print("Finished creating plant instances.")

    try:
        garden.add_plant(tomato)
        garden.add_plant(lettuce)
        garden.add_plant(carrot)
    except PlantError as e:
        print(f"Add error: {e}")
    finally:
        print("Finished adding plants to garden.")

    # try:
    #     garden.add_plant(None)  # invalid
    # except PlantError as e:
    #     print(f"Add error: {e}")
    # finally:
    #     print("Finished attempting to add invalid plant.")

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plant health...")
    try:
        print(GardenManager.check_plant_health(tomato))
        print(GardenManager.check_plant_health(lettuce))
        print(GardenManager.check_plant_health(carrot))
    except PlantError as e:
        print(f"Health error: {e}")
    finally:
        print("Finished health checks.")

    print("\nWatering plants repeatedly...")
    garden.water_plants()
    garden.water_plants()
    garden.water_plants()

    print("\nRe-checking plant health...")
    try:
        print(GardenManager.check_plant_health(tomato))
        print(GardenManager.check_plant_health(lettuce))
        print(GardenManager.check_plant_health(carrot))
    except PlantError as e:
        print(f"Health error: {e}")
    finally:
        print("System recovered and continued operation.")

    print("\nSystem still operational after errors ✔")


if __name__ == "__main__":
    test_garden_management()
