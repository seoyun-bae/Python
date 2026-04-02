import random

count = 0
N = 1000

for i in range(N):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 + dice2 == 6:
        count += 1

print("1000번 던져서 합이 6이 나온 횟수:", count)
print("실험적 확률:", count / N)
print("이론적 확률:", 5/36)