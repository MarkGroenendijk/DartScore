import numpy as np

score = 501

while score != 0:
    points = int(input())

    if points <= score:
        score -= points
    print(score)
print("you've won")
