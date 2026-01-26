#!/usr/bin/env python3


def check_temperature(temp_str: str) -> None:
    """Check if a temperature is within the acceptable range for plants."""
    try:
        x = int(temp_str)
        if x < 0:
            print(f"Error: {x}°C is too cold for plants (min 0°C)")
        elif x > 40:
            print(f"Error: {x}°C is too hot for plants (max 40°C)")
        else:
            print(f"Error: Temperature {x}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number!")


def test_temperature_inputs():
    """Test various temperature inputs."""
    test_inputs = ["25", "abc", "100", "-50"]
    for temp in test_inputs:
        print(f"\nTesting temperature: {temp}")
        check_temperature(temp)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_inputs()
    print("\n\nAll tests completed - program didn't crash!")
