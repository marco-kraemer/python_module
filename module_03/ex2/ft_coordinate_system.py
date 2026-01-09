#!/usr/bin/env python3

import sys
import math

def parse_coordinates(str):
    try:
        coordinates = str.split(",")
        x = int(coordinates[0])
        y = int(coordinates[1])
        z = int(coordinates[2])
        return (x, y, z)
    except ValueError:
        print("Value Error: Invalid coordinates")
    except IndexError:
        print("Index Error: Invalid coordinates")

def get_distance(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )

print("=== Game Coordinate System ===")

position = "10, 20, 5"
print(f"Position created: (10, 20, 5)")
coordinates = parse_coordinates(position)

print(f"{coordinates}")

distance = get_distance((0,0,0), coordinates)
print(f"Distance between (0, 0, 0) and (10, 20, 5): {distance:,.2f}")