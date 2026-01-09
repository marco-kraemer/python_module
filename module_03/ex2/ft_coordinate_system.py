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
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type {type(e).__name__}, Args: {e.args}")
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


print(f"\n\nPosition created: (10, 20, 5)")
position = "10, 20, 5"
coordinates = parse_coordinates(position)
distance = get_distance((0,0,0), coordinates)
print(f"Distance between (0, 0, 0) and (10, 20, 5): {distance:,.2f}")

print("\n\nParsing coordinates: (3,4,0)")
coordinates = parse_coordinates("3, 4, 0")
distance = get_distance((0,0,0), coordinates)
print(f"Distance between (0, 0, 0) and (3, 4, 0): {distance:,.1f}")

print(f"\n\nParsing invalid coordinates: (abc, def, ghi)")
parse_coordinates("abc,def,ghi")

print("\n\nUnpacking demonstration:")
x,y,z = coordinates
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")