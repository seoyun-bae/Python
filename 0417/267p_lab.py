score = [10, 12, 13, 9, 8, 11]
print("제거전=", score)

score.remove(max(score))
score.remove(min(score))

print("제거후=", score)