#!/usr/bin/env python3

print("=== Game Analytics Dashboard ===\n")

print("=== List Comprehension Examples ===")
players = ["alice", "bob", "charlie", "diana"]
scorers = [2300, 1800, 2150, 2050]

high_scorers = []
for i in range(len(players)):
    if scorers[i] > 2000:
        high_scorers.append(players[i])
print(f"High scorers (>2000): {high_scorers}")
doubled_scores = [i * 2 for i in scorers]
print(f"scores doubled: {doubled_scores}")
active_players = players[:-1]
print(f"Active players: {active_players}")

print("\n=== Dict Comprehension Examples ===")

players_scores = {
    "alice": 2300,
    "bob": 2800,
    "charlie": 2150,
    "diana": 2050
}

score_categories = {
    "high": 3,
    "medium": 2,
    "low": 1
}

achievement_count = {
    "alice": 5,
    "bob": 3,
    "charlie": 2,
    "diana": 6
}

player_stats = {
    "alice": {"score": 2300, "achievement": 5},
    "bob": {"score": 1800, "achievement": 3},
    "charlie": {"score": 2150, "achievement": 2},
    "diana": {"score": 2050, "achievement": 6}
}

total_score = 0
top_player = None
highest_value = 0
print(f"Player scores: ", end="")
for player_name, stats in player_stats.items():
    for key, value in stats.items():
        if key == "score":
           print(f"{player_name}: {value}, ", end="")
           if value > highest_value:
               highest_value = value
               player_highest_value = player_name
        total_score += value

print(f"\nScore categories: {score_categories}")
print(f"Total Score: {total_score}")
print(f"Achievement scores: ", end="")
for player_name, stats in player_stats.items():
    for key, value in stats.items():
        if key == "achievement":
           print(f"{player_name}: {value}, ", end="")

print("\n\n=== Set Comprehension Examples ===")
players = {"alice", "bob", "charlie", "diana", "alice"}
all_achievements = {"boss_slayer",
                    "collector",
                    "first_kill",
                    "level_10",
                    "perfectionist",
                    "speed_demon",
                    "treasure_hunter"}
regions = {"north", "east", "central"}

print(f"Unique players: {players}")
print(f"Unique achievements: {all_achievements}")
print(f"Active regions: {regions}")

print("\n=== Combined Analysis ===")
print(f"Total player: {len(players)}")
print(f"Total unique achievements: {all_achievements}")
avg_score = total_score / len(player_stats)
print(f"Average score: {avg_score}")
print(f"Top performer: {player_highest_value} ({highest_value} points, {achievement_count['alice']} achievements)")
