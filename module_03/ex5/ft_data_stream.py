#!/usr/bin/env python3

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime():
    a = 2
    while True:
        nbr = 2
        for nbr in range(2, a):
            if a % nbr == 0:
                nbr = 2
                a += 1
        yield a
        a += 1

def games_events(nbr):
    events = [
        "killed monster",
        "found treasure",
        "leveled up",
        "completed quest",
        "crafted item",
        "opened chest",
        "defeated boss",
        "learned new skill",
        "entered dungeon",
        "escaped ambush"
    ]

    players = [
        "alice",
        "bob",
        "charlie",
    ]

    for n in range(nbr):
        level = (n * 7) % 20 + 1
        player = players[n % len(players)]
        event = events[n % len(events)]
        yield n + 1, player, level, event
    

print("=== Game Data Stream Processor ===\n")

print("\nProcessing 1000 game events...\n")

high_level_players = 0
treasure_events = 0
level_up_events = 0
for index, player, level, event in games_events(100):
    print(f"Event {index}: Player {player} ({level}) {event}")
    if event == "found treasure":
        treasure_events += 1
    elif event == "leveled up":
        level_up_events += 1
    if level >= 10:
        high_level_players += 1

print("\n=== Stream Analytics ===")
print(f"Total events processed: {index}")
print(f"High-level players (10+): {high_level_players}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}")

print("\n=== Generator Demonstration ===")
print("Fibonacci sequence (first 10): ", end="")
count = 0
for n in fib():
    if count == 9:
        print(n)
        break
    print(f"{n}, ", end="")
    count += 1

print("\nPrime numbers (first 5): ", end="")
count = 0
for n in prime():
    if count == 4:
        print(n)
        break
    print(f"{n}, ", end="")
    count += 1