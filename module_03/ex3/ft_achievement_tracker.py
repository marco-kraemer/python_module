#!/usr/bin/env python3

class Player:
    def __init__(self, name):
        self.name = name
        self.achievements = set()
          
    def add_achievement(self, achievement, all_achievements):
        if achievement in all_achievements:
            self.achievements.add(achievement)
        else:
            print("Invalid achievement")


print("=== Achievement Tracker System ===")

all_achievements = {"boss_slayer",
                    "collector",
                    "first_kill",
                    "level_10",
                    "perfectionist",
                    "speed_demon",
                    "treasure_hunter"}

alice = Player("alice")
alice.add_achievement("first_kill", all_achievements)
alice.add_achievement("level_10", all_achievements)
alice.add_achievement("treasure_hunter", all_achievements)
alice.add_achievement("speed_demon", all_achievements)

bob = Player("bob")
bob.add_achievement("first_kill", all_achievements)
bob.add_achievement("level_10", all_achievements)
bob.add_achievement("boss_slayer", all_achievements)
bob.add_achievement("collector", all_achievements)

charlie = Player("charlie")
charlie.add_achievement("level_10", all_achievements)
charlie.add_achievement("treasure_hunter", all_achievements)
charlie.add_achievement("boss_slayer", all_achievements)
charlie.add_achievement("speed_demon", all_achievements)
charlie.add_achievement("perfectionist", all_achievements)

print(f"Player alice achievements: {alice.achievements}")
print(f"Player bob achievements: {bob.achievements}")
print(f"Player charlie achievements: {charlie.achievements}")

print("\n\n=== Achievement Analytics ===")

unique_achievements = (alice.achievements |
                       bob.achievements |
                       charlie.achievements)

print(f"All unique achievements {unique_achievements}")
print(f"Total unique achievements: {len(unique_achievements)}")

common_achievements = (alice.achievements &
                       bob.achievements &
                       charlie.achievements)

print(f"\n\nCommon to all players {common_achievements}")

rare_achievements = (alice.achievements - bob.achievements - charlie.achievements |
                     bob.achievements - alice.achievements - charlie.achievements |
                     charlie.achievements - alice.achievements - bob.achievements)

print(f"Rare achievements (1 player): {rare_achievements}")

print(f"\n\nAlice vs Bob common: {alice.achievements & bob.achievements}")
print(f"Alice unique: {alice.achievements - bob.achievements}")
print(f"Bob unique: {bob.achievements - alice.achievements}")