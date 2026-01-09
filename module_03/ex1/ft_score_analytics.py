#!/usr/bin/env python3

import sys

arguments = sys.argv
arguments = arguments[1:]
scores = []
try :
    for argument in arguments:
        scores.append(int(argument))
except ValueError:
    print("Invalid Score")
    sys.exit(1)
print("=== Player Score Analytics ===")
if len(scores) == 0:
    print("No score provided. Usage: python3 ft_score_analytics.c <score1> <score2> ...")
    sys.exit(1)
print(f"Total Players: {len(scores)}")
print(f"Total score: {sum(scores)}")
avg = sum(scores) / len(scores)
print(f"Average score: {avg}")
print(f"High Score: {max(scores)}")
print(f"Low score: {min(scores)}")
print(f"Score range: {max(scores) - min(scores)}")