import random

board = [['#' if random.random() < 0.3 else '.' for _ in range(10)] for _ in range(10)]

for row in board:
    print(" ".join(row))