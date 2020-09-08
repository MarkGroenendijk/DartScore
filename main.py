import numpy as np

# Get player count
print("How many players are up for a game?")
player_count = int(input())
while player_count <= 0:
    print("Invalid player count please retry.")
    player_count = int(input())

# Add initial scores to array
score = []
for i in range(player_count):
    score.append(501)

breaker = True
while breaker:
    for i, elem in enumerate(score):
        print(f"How many points did player {i} score?")
        points = int(input())

        if points == elem:
            print(f"Player {i} won")
            breaker = False
            break
        if points < elem:
            score[i] -= points
            print(f"player {i} now has {score[i]} points")
        else:
            print(f"player {i} overthrew, {score[i]} points remaining")




