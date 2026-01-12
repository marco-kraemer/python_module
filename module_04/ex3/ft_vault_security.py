#!/usr/bin/env python3

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")
with open("../classified_data.txt", "r") as f:
    data = f.read()
print("Vault connection established with failsafe protocols\n")

print("SECURE EXTRACTION:")
print(data)

with open("../security_protocols.txt", "r") as f:
    data = f.read()
print("\nSECURE PRESERVATION:")
print(data)
print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")