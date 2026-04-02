import random

x = random.randint(1, 100)
y = random.randint(1, 100)
answer = int(input(f"{x} + {y} = "))
if answer == x + y :
    print("잘했어요!")
else :
    print("틀렸어요!")
