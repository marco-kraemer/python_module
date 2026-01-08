#!/usr/bin/env python3

def garden_operations():
    try:
        print("\n\nTesting ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print("\n\nTesting ZeroDivisionError...")
        x = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("\n\nFileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        print("\n\nTesting KeyError...")
        plants = {
            "rose" : 60,
            "oak" : 30
        }
        value = plants["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    garden_operations()
    
    print("\n\nTesting multiple errors together...")
    try:
        data = {}
        int("hello") / data["key"]
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")
    print("\n\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()