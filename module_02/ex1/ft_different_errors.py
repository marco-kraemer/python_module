#!/usr/bin/env python3


def garden_operations() -> None:
    """Perform various garden operations that may raise different errors."""
    try:
        print("\n\nTesting ValueError...")
        int("abc")
    except ValueError as e:
        print("Caught ValueError:", e)
    try:
        print("\n\nTesting ZeroDivisionError...")
        _ = 10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    try:
        print("\n\nFileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    try:
        print("\n\nTesting KeyError...")
        plants = {"rose": 60, "oak": 30}
        _ = plants["missing_plant"]
    except KeyError as e:
        print("Caught KeyError:", e)


def test_error_types() -> None:
    """Test various error types in garden operations."""

    garden_operations()

    print("\n\nTesting multiple errors together...")
    try:
        data: dict = {}
        int("hello") / data["key"]
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\n\nAll error types tested successfully!")
