#!/usr/bin/env python3

import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
archivist_id = input("Input Stream active. Enter archivist ID:")
report = input("Input Stream active. Enter status report:")

sys.stdout.write(f"\n{{[}}STANDARD{{]}} Archive status from {archivist_id}: {report}\n")
sys.stderr.write(f"{{[}}ALERT{{]}} System diagnostic: Communication channels verified\n")
sys.stdout.write(f"{{[}}STANDARD{{]}} Data transmission complete\n")

print("\nThree-channel communication test successful.")