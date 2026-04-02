import random

total = 10000000
count = 0

for i in range(total):
    x = random.random()
    y = random.random()
    if x*x + y*y <= 1:
        count += 1

pi= (count / total) * 4
print(f"파이의 값은 {pi}입니다.")
