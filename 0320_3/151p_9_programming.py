import random

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
op = random.randint(1, 4)

if op == 1:
    answer = float(input(f"{n1} + {n2}의 값은? "))
    if answer == n1 + n2:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")

elif op == 2:
    answer = float(input(f"{n1} - {n2}의 값은? "))
    if answer == n1 - n2:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")

elif op == 3:
    answer = float(input(f"{n1} * {n2}의 값은? "))
    if answer == n1 * n2:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")

elif op == 4:
    answer = float(input(f"{n1} / {n2}의 값은? "))
    if answer == n1 / n2:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
