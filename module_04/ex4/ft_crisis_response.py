#!/usr/bin/env python3

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
try:
    with open("lost_archive.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handles, security maintained")

print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
try:
    with open("classified_vault.txt", "r") as f:
        f.read()
except PermissionError:
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")

print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt")
try:
    with open("../standard_archive.txt", "r") as f:
        f.read()
        print("SUCCESS: Archive recovered - ``Knowledge preserved for humanity''")
        print("STATUS: Normal operations resumed")
except:
    print("Error")

print("\nAll crisis scenarios handled successfully. Archives secure.")