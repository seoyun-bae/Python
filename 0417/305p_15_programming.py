coins = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
print(coins)

max_streak = 0
current_streak = 1

for i in range(len(coins)-1):
    if coins[i] == coins[i+1]:
        current_streak += 1
    else:
        if current_streak > max_streak:
            max_streak = current_streak
        current_streak = 1
max_streak = max(max_streak, current_streak)
print(f"최대 연속 길이 = {max_streak}")