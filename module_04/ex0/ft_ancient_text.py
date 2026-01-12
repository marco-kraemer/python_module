#!/usr/bin/env python3

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

print("Acessing Storage Vault: ancient_fragment.txt")
f = open("../ancient_fragment.txt", "r")
print("Connection established...\n")
print("RECOVERED DATA:")
print(f.read())
print("\nData recovery complete. Storage unit disconnected.")
f.close()
