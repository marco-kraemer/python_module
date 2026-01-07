#!/usr/bin/env python3

def check_temperature(temp_str):
    try:
        x = int(temp_str)
        if x < 0:
            print(f"{x}°C is too cold for plants (min 0°C)")
        elif x > 40:
            print(f"{x}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {x}°C is perfect for plants!")
    except:
        print(f"'{temp_str}' is not a valid number!")

if __name__ == "__main__":
    check_temperature("hello")
    check_temperature(50)
    check_temperature(-5)
    check_temperature(0)
    check_temperature(10)